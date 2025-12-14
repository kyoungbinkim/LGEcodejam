from sys import stdin
from collections import deque

rl = stdin.readline
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

n, m = map(int, rl().split())
b = [list(map(int, rl().split())) for _ in range(n)]
links = [[] for _ in range(n*m)]
deg = [0 for _ in range(n*m)]
cnts = [0 for _ in range(n*m)]
cnts[0] = 1
ans = 0

for i in range(n):
    for j in range(m):
        for di, dj in dirs:
            mi, mj = i+di, j+dj
            if 0 <= mi < n and 0 <= mj < m and b[i][j] > b[mi][mj]:
                deg[mi*m + mj] += 1
                links[i*m + j].append(mi*m + mj)

q = deque()
for i in range(n*m):
    if deg[i] == 0:
        q.append(i)


while q:
    idx = q.popleft()
    x,y  = idx // m, idx % m
    
    for nxt in links[idx]:
        if nxt == n*m-1:
            ans += cnts[idx]
            continue
        cnts[nxt] += cnts[idx]
        deg[nxt] -= 1
        if deg[nxt] == 0:
            q.append(nxt)
print(ans)
    

