from sys import stdin
from collections import deque

n,m = map(int, stdin.readline().split())
deg = [0 for _ in range(n+1)]
max_path = [0 for _ in range(n+1)]

board = {i:[] for i in range(1, n+1)}
q = deque()

for _ in range(m):
    s,e = map(int, stdin.readline().split())
    board[s].append(e)
    deg[e] += 1

for i in range(1, n+1):
    if deg[i] == 0:
        q.append(i)

while q:
    idx = q.popleft()
    
    for next in board[idx]:
        deg[next] -= 1
        max_path[next] = max(max_path[next],max_path[idx]+1)
        
        if deg[next] == 0:
            q.append(next)
print(max(max_path))