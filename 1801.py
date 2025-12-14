from sys import stdin
import random
n = int(stdin.readline())
b = list(map(int, stdin.readline().split()))


bm = {}
for i in range(1, 11):
    if i in b:
        bm[i] = b.count(i)
bm_keys = sorted(list(bm.keys()))

sumb = sum(b)

dp = [set() for _ in range(sum(b) // 2 )]
dp[0].add(tuple([0 for _ in range(11)]))
for i in range(len(dp)):
    
    for j in bm_keys:
        if j > i:
            break
        
        for d in dp[i-j]:
            if d[j] == bm[j]:
                continue
            tmp = tuple([ _k if _i != j else _k+1 for _i, _k in enumerate(d)])
            dp[i].add(tmp)
    
update = [[]]

for i in range(1, len(dp)):
    tmp = set()
    l = list(dp[i])
    for j in range(len(l)):
        for k in range(j, len(l)):
            new = tuple([_j+_k for _j,_k in zip(l[j], l[k])])
            
           
            if any( [new[i] > bm[i] if bm.get(i) else False for i in range(11)]):
                continue
            
            tmp.add(new)
    update.append(list(tmp))

ans = -1
for i in range(1, len(update)):
    for j in range(i, len(update)):
        if i+j > sumb//2:
            continue
        
        for ui in update[i]:
            for uj in update[j]:
                if any([ False  if ui[idx] + uj[idx] ==0  else ui[idx] + uj[idx]>bm[idx]  for idx in range(11)]):
                    continue
                ans= max(ans, i*j)
print(ans)