from sys import stdin
from heapq import heappush, heappop

N,M = map(int,stdin.readline().split())

dir = {i : [] for i in range(1, N+1)}
cost = [[None for _ in range(N+1)] for _ in range(N+1)]
dp = [(1, float('inf')) for _ in range(N+1)]
dp[1] = (float('inf'), 0)

h = [] # min_f/sum_c, min_f, sum_c, start_idx, end_idx

for _ in range(M):
    a,b,c,f = map(int, stdin.readline().split())
    
    cost[a][b] = cost[b][a] = (c,f)
    
    dir[a].append(b)
    dir[b].append(a)


for e in dir[1]:
    _c, _f = cost[1][e]
    heappush(h, (-_f/_c, _f, _c, 1, e))

while h:
    ratio, _f, _c, s_idx, e_idx = heappop(h)
    
    if dp[e_idx][0] / dp[e_idx][1] < _f/ _c :
        dp[e_idx] = (_f, _c)
    
    for _e in dir[e_idx]:
        _c, _f = cost[e_idx][_e]
        if dp[_e][1] == float('inf'):
            heappush(h, (-min(_f, dp[e_idx][0])/(dp[e_idx][1] + _c), min(_f, dp[e_idx][0]), dp[e_idx][1] + _c, e_idx, _e))

    # print(dp)
print(int(dp[-1][0]/dp[-1][1] * 1_000_000))