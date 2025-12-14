from sys import stdin
from random import randint

rl = stdin.readline

n, c = map(int, rl().split())

dp = []
hi = [int(rl()) for _ in range(n)]
maxh = max(hi)+1

for h in hi:
    
    # h = randint(1, 100)
    update = []
    for h_, up in zip(range(h, maxh+1), range(maxh-h)):
        tmp = [h_, float('inf')]
        up *= up
        if dp == []:
            update.append([h_, up])
            continue
        for d, v  in dp:
            tmp[1] = min(tmp[1], v+abs(d-h_)*c + up)
        update.append(tmp)
    # print(update)
    dp = update

print(min([d[1] for d in dp]))