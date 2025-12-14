from sys import stdin
from collections import deque

dimen = list(map(int, stdin.readline().split()))
acc = [1, dimen[0]]

for i in range(1, 11):
    acc.append(acc[-1]*dimen[i])

b = []
q = deque()
for i in range(acc[-1] // acc[1]):
    
    l = list(map(int, stdin.readline().split()))
    
    for j in range(dimen[0]):
        if l[j] == 1:
            q.append((len(b) + j, 0))
    b += l

while q:
    idx, cnt = q.popleft()
    
    for i in range(11):
        dIdx = idx // acc[i] % dimen[i]
        
        if dIdx >= 1 and b[idx- acc[i]] == 0:
            b[idx - acc[i]]  = 1
            q.append((idx - acc[i], cnt+1))
            
        
        if dIdx < dimen[i]-1 and b[idx + acc[i]] == 0:
            b[idx + acc[i]] = 1
            q.append((idx + acc[i], cnt+1))
    
for i in range(len(b)):
    if b[i] == 0:
        cnt = -1
        break
print(cnt)
            






    
# 6 4 2 2 1 1 1 1 1 1 1

# 6 4 2 2 2 2 2 2 2 2 2