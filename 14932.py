from sys import stdin
from collections import deque

dir = {
    'U' : (-1,0),
    'D' : (1,0),
    'L' : (0, -1),
    'R' : (0, 1)
}

def move(mvStr):
    d = dir[mvStr[-1]]
    _mv = int(mvStr[:-1])
    return (d[0]*_mv, d[1]*_mv)

n = int(stdin.readline())

visit = set()
g = [[] for _ in range(n*n+1)]
deg = [0 for _ in range(n*n+1)]
for i in range(n):
    for j,mv in enumerate(stdin.readline().split()):
        d = move(mv)
        di,dj = i + d[0], j+1 + d[1]
        
        g[n*i+j+1].append(di*n + dj)
        deg[di*n + dj] += 1


q = deque()

for i in range(1, n*n+1):
    if deg[i] == 0:
        q.append(i)


if len(q) > 1:
    print("TOO SAFE")
elif len(q) == 1:
    
    
    
    cur = q.popleft()
    ans = cur
    visit = set([cur])
    while True:
        nxt = g[cur][0]
        
        if nxt in visit:
            break
        
        visit.add(nxt)
        cur = nxt
    print( f"{ans//n + 1} {ans%n}"  if len(visit) == n*n else 'TOO SAFE')
else:
    
    cur = 1
    visit = set([cur])
    
    while True:
        nxt = g[cur][0]
        
        if nxt in visit:
            break
        visit.add(nxt)
        cur = nxt
    print( 'THIEF LOVE IT!' if len(visit) == n*n else 'TOO SAFE')