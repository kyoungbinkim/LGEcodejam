from sys import stdin
from collections import deque
from copy import deepcopy

dir = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

c2n = {
    '.': 0,
    'W' : float('inf')
}

def solve():
    n, m, cnt, r, c = map(int, stdin.readline().split())
    
    dest = []
    for _ in range(cnt):
        dest.append(tuple(map(lambda x:int(x)-1, stdin.readline().split())))
        
    board = [list(map(lambda x: c2n[x], stdin.readline().strip())) for _ in range(n)]
    tmp = deepcopy(board)
    
    
    