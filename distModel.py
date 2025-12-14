import os
import math
import inspect
import threading
from dataclasses import dataclass


import torch
import torch.nn as nn
from torch.nn import functional as F

from torch.distributed.rpc import RRef
import torch.distributed.rpc as rpc



class LayerNorm(nn.Module):
      """ LayerNorm but with an optional bias. PyTorch doesn't support simply bias=False """

      def __init__(self, ndim, bias):
            super().__init__()
            self.weight = nn.Parameter(torch.ones(ndim))
            self.bias = nn.Parameter(torch.zeros(ndim)) if bias else None

      def forward(self, input):
            return F.layer_norm(input, self.weight.shape, self.weight, self.bias, 1e-5)

class CausalSelfAttention(nn.Module):

      def __init__(self, config):
            super().__init__()
            assert config.n_embd % config.n_head == 0
            # key, query, value projections for all heads, but in a batch
            self.c_attn = nn.Linear(config.n_embd, 3 * config.n_embd, bias=config.bias)
            # output projection
            self.c_proj = nn.Linear(config.n_embd, config.n_embd, bias=config.bias)
            # regularization
            self.attn_dropout = nn.Dropout(config.dropout)
            self.resid_dropout = nn.Dropout(config.dropout)
            self.n_head = config.n_head
            self.n_embd = config.n_embd
            self.dropout = config.dropout
            # flash attention make GPU go brrrrr but support is only in PyTorch >= 2.0
            self.flash = hasattr(torch.nn.functional, 'scaled_dot_product_attention')
            if not self.flash:
                  print("WARNING: usinginput slow attention. Flash Attention requires PyTorch >= 2.0")
                  # causal mask to ensure that attention is only applied to the left in the input sequence
                  self.register_buffer("bias", torch.tril(torch.ones(config.block_size, config.block_size))
                                          .view(1, 1, config.block_size, config.block_size))

      def forward(self, x):
            B, T, C = x.size() # batch size, sequence length, embedding dimensionality (n_embd)

            # calculate query, key, values for all heads in batch and move head forward to be the batch dim
            q, k, v  = self.c_attn(x).split(self.n_embd, dim=2)
            k = k.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)
            q = q.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)
            v = v.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)

            # causal self-attention; Self-attend: (B, nh, T, hs) x (B, nh, hs, T) -> (B, nh, T, T)
            if self.flash:
                  # efficient attention using Flash Attention CUDA kernels
                  y = torch.nn.functional.scaled_dot_product_attention(q, k, v, attn_mask=None, dropout_p=self.dropout if self.training else 0, is_causal=True)
            else:
                  # manual implementation of attention
                  att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))
                  att = att.masked_fill(self.bias[:,:,:T,:T] == 0, float('-inf'))
                  att = F.softmax(att, dim=-1)
                  att = self.attn_dropout(att)
                  y = att @ v # (B, nh, T, T) x (B, nh, T, hs) -> (B, nh, T, hs)
            y = y.transpose(1, 2).contiguous().view(B, T, C) # re-assemble all head outputs side by side

            # output projection
            y = self.resid_dropout(self.c_proj(y))
            return y

class MLP(nn.Module):

      def __init__(self, config):
            super().__init__()
            self.c_fc    = nn.Linear(config.n_embd, 4 * config.n_embd, bias=config.bias)
            self.gelu    = nn.GELU()
            self.c_proj  = nn.Linear(4 * config.n_embd, config.n_embd, bias=config.bias)
            self.dropout = nn.Dropout(config.dropout)

      def forward(self, x):
            x = self.c_fc(x)
            x = self.gelu(x)
            x = self.c_proj(x)
            x = self.dropout(x)
            return x

class Block(nn.Module):

    def __init__(self, config):
        super().__init__()
        self.ln_1 = LayerNorm(config.n_embd, bias=config.bias)
        self.attn = CausalSelfAttention(config)
        self.ln_2 = LayerNorm(config.n_embd, bias=config.bias)
        self.mlp = MLP(config)

    def forward(self, x):
        x = x + self.attn(self.ln_1(x))
        x = x + self.mlp(self.ln_2(x))
        return x

class DistBlock(nn.Module):

      def __init__(self, config, is_last=False):
            super().__init__()
            self._lock = threading.Lock() # 다중 스레드에서 사용할 수 있는 락
            self.ln_1 = LayerNorm(config.n_embd, bias=config.bias) 
            self.attn = CausalSelfAttention(config)
            self.ln_2 = LayerNorm(config.n_embd, bias=config.bias)
            self.mlp = MLP(config)
            if is_last:
                  self.ln_f = LayerNorm(config.n_embd, bias=config.bias)

      def parameter_rrefs(self):
            return [RRef(p) for p in self.parameters()]

      def forward(self, x_rref):
            x = x_rref.to_here()
            with self._lock:
                  x = x + self.attn(self.ln_1(x))
                  x = x + self.mlp(self.ln_2(x))
            return x.cpu()


class DistBlockShard(nn.Module):
      def __init__(
            self, 
            config, 
            layers_per_worker:int,
            is_last: bool = False
      ):
            super().__init__()
            self._lock = threading.Lock()
            
            print(f"DistBlockShard config : {config }")
            print(f"DistBlockShard layers_per_worker : {layers_per_worker}")            
            print(f"is_last : {is_last}")
            config.device = 'cuda' if torch.cuda.is_available() else 'cpu'
            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

            self.blocks = [Block(config).to(self.device) for _ in range(layers_per_worker)]
            self.layers_per_worker = layers_per_worker
            self.is_last = is_last
            if self.is_last:
                  self.ln_f = LayerNorm(config.n_embd, bias=config.bias).to(self.device)
                  self.lm_head = nn.Linear(config.n_embd, config.vocab_size, bias=False).to(self.device)

            for pn, p in self.named_parameters():
                  if pn.endswith('c_proj.weight'):
                        torch.nn.init.normal_(p, mean=0.0, std=0.02/math.sqrt(2 * config.n_layer))
            
      # 학습을 위해 모델의 파라미터를 반환
      def parameter_rrefs(self):
            return [RRef(p) for p in self.parameters()] 
            
      def forward(self, x_rref, form='train'):
            x = x_rref.to_here().to(self.device)
            
            with self._lock:
                  for block in self.blocks:
                        x = block(x)
                  if self.is_last:
                        x = self.ln_f(x)
                        if form == 'train':
                              x = self.lm_head(x)
                        elif form == 'generate':
                              x = self.lm_head(x[:, [-1], :])
            return x.cpu()
      
@dataclass
class GPTConfig:
      block_size: int = 1024
      vocab_size: int = 50304 # GPT-2 vocab_size of 50257, padded up to nearest multiple of 64 for efficiency
      n_layer: int = 12
      n_head: int = 12
      # n_embd: int = 768
      n_embd: int = 384
      dropout: float = 0.1
      bias: bool = True # True: bias in Linears and LayerNorms, like GPT-2. False: a bit better and faster
      worker_num: int = 1
      device: str = 'cpu'

class DistGPT(nn.Module):
      def __init__(
            self, 
            config, 
            workers,
            *args,
            **kwargs
      ):
            super().__init__()
            assert config.vocab_size is not None
            assert config.block_size is not None
            assert config.n_layer % config.worker_num == 0
            assert config.worker_num == len(workers) 
            
            self.config = config
            
            self.transformer = nn.ModuleDict(dict(
                  wte = nn.Embedding(config.vocab_size, config.n_embd),
                  wpe = nn.Embedding(config.block_size, config.n_embd),
                  drop = nn.Dropout(config.dropout),
            ))
            
            self.layers_per_worker = config.n_layer // config.worker_num
            self.h_rref = [ ]
            for idx in range(self.config.worker_num):
                  self.h_rref.append(
                        rpc.remote(
                              workers[idx],
                              DistBlockShard,
                              args = (self.config, self.layers_per_worker, idx==self.config.worker_num-1, ),
                              kwargs = kwargs
                        )
                  )
            
            self.lm_head = nn.Linear(config.n_embd, config.vocab_size, bias=False)
            

      def parameter_rrefs(self):
            remote_params = []

            for block_rref in self.h_rref:
                  remote_params.extend(block_rref.remote().parameter_rrefs().to_here())
            
            return remote_params
      
                  
      def forward(self, idx, targets=None):
            b, t = idx.size()
            assert t <= self.config.block_size, f"Cannot forward sequence of length {t}, block size is only {self.config.block_size}"
            pos = torch.arange(0, t, dtype=torch.long, ) #

            # forward the GPT model itself
            tok_emb = self.transformer.wte(idx) # token embeddings of shape (b, t, n_embd)
            pos_emb = self.transformer.wpe(pos) # position embeddings of shape (t, n_embd)
            x = self.transformer.drop(tok_emb + pos_emb)
            x_rref = RRef(x)
            
            for block in self.h_rref[:-1]:
                  x_rref = block.remote().forward(x_rref)
            
            if targets is not None:
                  logits = self.h_rref[-1].rpc_async().forward(x_rref, 'train').wait()
                  loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1), ignore_index=-1)
            else:
                  logits = self.h_rref[-1].rpc_async().forward(x_rref, 'generate').wait()
                  loss = None
            
            return logits, loss
      
      @torch.no_grad()
      def generate(self, idx, max_new_tokens, temperature=1.0, top_k=None):
            """
            Take a conditioning sequence of indices idx (LongTensor of shape (b,t)) and complete
            the sequence max_new_tokens times, feeding the predictions back into the model each time.
            Most likely you'll want to make sure to be in model.eval() mode of operation for this.
            """
            for _ in range(max_new_tokens):
                  # if the sequence context is growing too long we must crop it at block_size
                  idx_cond = idx if idx.size(1) <= self.config.block_size else idx[:, -self.config.block_size:]
                  # forward the model to get the logits for the index in the sequence
                  
                  logits, _ = self.forward(idx_cond)
                  # pluck the logits at the final step and scale by desired temperature
                  logits = logits[:, -1, :] / temperature
                  # optionally crop the logits to only the top k options
                  if top_k is not None:
                        v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                        logits[logits < v[:, [-1]]] = -float('Inf')
                  # apply softmax to convert logits to (normalized) probabilities
                  probs = F.softmax(logits, dim=-1)
                  # sample from the distribution
                  idx_next = torch.multinomial(probs, num_samples=1)
                  # append sampled index to the running sequence and continue
                  idx = torch.cat((idx, idx_next), dim=1)

            return idx

      
            
import numpy as np
data_dir = os.path.join('./')
def get_batch(split, block_size = 1024, batch_size=2):
    # We recreate np.memmap every batch to avoid a memory leak, as per
    # https://stackoverflow.com/questions/45132940/numpy-memmap-memory-usage-want-to-iterate-once/61472122#61472122
    if split == 'train':
        data = np.memmap(os.path.join(data_dir, 'train.bin'), dtype=np.uint16, mode='r')
    else:
        data = np.memmap(os.path.join(data_dir, 'val.bin'), dtype=np.uint16, mode='r')
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([torch.from_numpy((data[i:i+block_size]).astype(np.int64)) for i in ix])
    y = torch.stack([torch.from_numpy((data[i+1:i+1+block_size]).astype(np.int64)) for i in ix])
    
    return x, y


import pickle
meta_path = os.path.join('./', 'meta.pkl')
with open(meta_path, 'rb') as f:
      meta = pickle.load(f)
# TODO want to make this more general to arbitrary encoder/decoder schemes
stoi, itos = meta['stoi'], meta['itos']
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])