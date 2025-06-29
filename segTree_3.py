from sys import stdin

class segTree:
    
    def __init__(self, n ,leafs):
        self.bin_n = bin(n)
        self.leafs_num =  n if self.bin_n.count('1') == 1 else 2 ** (len(self.bin_n) - 2)
        self.leafs = leafs + [0 for _ in range(self.leafs_num - n)]
        
        self.tree = [-1 for _ in range(self.leafs_num)] + self.leafs
        
        self.buildTree(1)
        # print(self.tree[self.leafs_num])
    
    def buildTree(self, idx):
        if self.tree[idx] >= 0:
            return self.tree[idx]
        
        self.tree[idx] = self.buildTree(idx*2) + self.buildTree(idx * 2 + 1)
        
        return self.tree[idx]
    
    def updateTree(self, idx, val):
        self.tree[self.leafs_num+ idx -1] += val
        
        update_idx = (self.leafs_num+ idx -1) // 2
        while update_idx:
            self.tree[update_idx] += val
            update_idx = update_idx // 2
        
        # print(self.tree)
    
    def find(self, toFind):
        
        idx = 1
        acc = 0
        while idx < self.leafs_num:
            if self.tree[idx * 2] < toFind:
                toFind -= self.tree[idx*2]
                idx = idx * 2 + 1
            else:
                idx = idx * 2
        print(idx-self.leafs_num + 1)
        
        

n = int(stdin.readline())
l = list(map(int,stdin.readline().split()))
st = segTree(n, l)

for _ in range(int(stdin.readline())):
    cmd = list(map(int, stdin.readline().split()))
    
    # print(st.tree)
    if cmd[0] == 1:
        st.updateTree(cmd[1],cmd[2])
    
    else:
        st.find(cmd[1])
        

