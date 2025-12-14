from sys import stdin
from collections import deque
from copy import deepcopy

global ans
global visit

ans = float('inf')
visit = set()
n,m = map(int, stdin.readline().split())
board = [[s for s in stdin.readline().rstrip()] for _ in range(n)]

if board[n-1][m-1] == 'B' or board[0][0] == 'B':
    print(-1)
    exit()

next = {
    'A' : 'A',
    'B' : 'B',
    'C' : 'D',
    'D' : 'C'
}

dir = {
    'A' : [(0,1), (1,0), (0,-1), (-1,0)],
    'B' : [],
    'C' : [(1,0), (-1, 0)],
    'D' : [(0,1), (0,-1)]
}

def rotate(rot, i, j):
    next = rot
    next = next ^ (1 << i)
    next = next ^ (1 << j+n)
    # print(bin(rot), i, j, bin(next))
    return next

def getNtBbit(n, nth):
    return 1 if n&(1 << nth) else 0

def getAlpha(b, i, j, rot):
    if getNtBbit(rot, i) + getNtBbit(rot, j+n) == 1:
        return next[b[i][j]]
    return b[i][j]

que = deque([(0,0,0, 0)])
visit.add((0,0,0))

while len(que):
    # print(que)
    x,y,rot, move = que.popleft()
    nextRot = rotate(rot, x, y)

    if getAlpha(board, x, y, rot) == 'B' or move >= ans:
        continue
    
    for (dx, dy) in dir[getAlpha(board, x, y, rot)]:
        # print(x,y,rot, move, dx, dy)
        mx, my = x+dx, y+dy

        if mx < 0 or mx >= n or my < 0 or my >= m:
            continue
        
        alpha = getAlpha(board, mx, my, rot)
        # print(alpha)
        if board[mx][my] != 'B' and \
            ((dy == 0 and  alpha != 'D') or \
             (dx == 0 and alpha != 'C')) and (mx, my, rot) not in visit:
            if mx == n-1 and my == m-1:
                ans = min(ans, move+1)
                
            que.append((mx, my, rot, move+1))
            visit.add((mx, my, rot))

        alpha = getAlpha(board, mx, my, nextRot)
        # print(alpha, nextRot)
        if board[mx][my] != 'B' and \
            ((dy == 0 and  alpha != 'D') or \
             (dx == 0 and alpha != 'C')) and (mx, my, nextRot) not in visit:
            if mx == n-1 and my == m-1:
                ans = min(ans, move+2)
                continue

            que.append((mx, my, nextRot, move+2))
            visit.add((mx, my, nextRot))
            

if ans == float('inf'):
    print(-1)
else:
    print(ans)

