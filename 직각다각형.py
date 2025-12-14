from  sys import stdin

dir = [
    (-1,0), (0,-1), (1,0), (0,1)
]

n = int(stdin.readline())

start = tuple(map(int, stdin.readline().split()))
bfr = start
for _ in range(n-1):
    nxt = tuple(map(int, stdin.readline().split()))

    dx = 0 if nxt[0] - bfr[0] == 0 else ((nxt[0] - bfr[0])// abs(nxt[0] - bfr[0]))
    dy = 0 if nxt[1] - bfr[1] == 0 else ((nxt[1] - bfr[1])// abs(nxt[1] - bfr[1]))

    print(bfr, nxt, dx, dy)

    bfr = nxt

    