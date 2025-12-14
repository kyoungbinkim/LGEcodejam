from sys import stdin
from collections import deque

bmap = {
    'E' : 0, 'H': 1
}
DIR = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1),
]


n = int(stdin.readline())
board = [
    [ bmap[c] for c in stdin.readline().strip()] for _ in range(n)
]

if n == 1:
    print(0)
    exit()

def turn_left(pos):
    return (pos[0], pos[1], (4+pos[2] - 1) % 4)

def turn_right(pos):
    return (pos[0], pos[1], (pos[2] + 1) % 4)

def batch_turn_left(poss):
    return (turn_left(poss[0]), turn_left(poss[1]))

def batch_turn_right(poss):
    return (turn_right(poss[0]), turn_right(poss[1]))
    
def go_straight(pos):
    if pos[0] == 0 and pos[1]== n-1:
        return pos

    d = DIR[pos[2]]    
    dx = pos[0] + d[0]
    dy = pos[1] + d[1]
    
    if dx <0 or dx >= n:
        dx = pos[0]
    
    if dy <0 or dy >= n:
        dy = pos[1]
    
    if board[dx][dy]:
        return pos
    
    return (dx, dy , pos[2])
    
def batch_go_straight(poss):
    return (go_straight(poss[0]), go_straight(poss[1]))

def is_visit(pos, v):
    if (pos[0], pos[1]) in v:
        return True
    # elif (pos[1], pos[0]) in v:
    #     return True
    return False


start = (
    ((n-1,0,2), (n-1,0,1)), 
    0
    )
visit = set([((n-1,0,2), (n-1,0,1))])
q = deque([start])
ans = -1

while q:
    cur, cnt = q.popleft()
    # print(f"cur : {cur}, cnt:{cnt}")
    # trun left
    l = batch_turn_left(cur)
    r = batch_turn_right(cur)
    mv= batch_go_straight(cur)
    
    if mv[0][0] == 0 and mv[0][1] == n-1 and mv[1][0] == 0 and mv[1][1] == n-1:
        ans = cnt+1
        break
    
    if not is_visit(l, visit):
        q.append((l, cnt+1))
        visit.add(l)
    
    if not is_visit(r, visit):
        q.append((r, cnt+1))
        visit.add(r)
        
    if not is_visit(mv, visit):
        q.append((mv, cnt+1))
        visit.add(mv)
    
print(ans)  