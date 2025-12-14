from sys import stdin
from collections import deque
from copy import deepcopy

rl = stdin.readline

b = {
    '.' : 0,
    '#' : 1
}

dir = [(0,1), (1,0), (0,-1), (-1,0), (0,0)]


n, m = map(int, rl().split())
g = {}
sx, sy, ex, ey = map(lambda x:int(x)-1, rl().split())

board = []

for i in range(n):
    s = rl().rstrip()
    
    l = []
    for j, c in enumerate(s):
        if c in b.keys():
            l.append(b[c])
        else:
            g[(i,j)] = int(c)
            l.append(1)
    
    board.append(l)

boards = []
for cnt in range(4):
    tmp = deepcopy(board)
    for gx,gy in g.keys():
        dx, dy = dir[(g[(gx,gy)] + cnt)%4]
        
        x,y = gx + dx, gy + dy
        
        while True:    
            if x<0 or x>= n or y <0 or y>= m:
                break
                
            if board[x][y] == 1:
                break
            
            tmp[x][y] = 2
            
            x += dx
            y += dy
        
    boards.append(tmp)

q = deque([(sx, sy , 0)])
visit = set([(sx, sy, 0)])
while q:
    x,y,t = q.popleft()
    
    for dx, dy in dir:
        mx, my = x+dx, y+dy
        
        if mx<0 or mx>=n or my <0 or my>=m or (mx, my, (t+1)%4) in visit:
            continue
        
        if board[mx][my] == 1 or boards[(t+1)%4][mx][my]:
            continue
            
        if (mx,my) == (ex, ey):
            print(t+1)
            exit()
        q.append((mx,my,t+1))
        visit.add((mx, my,(t+1)%4))
        
print('GG')