from sys import stdin
from heapq import heappop, heappush

n, k = map(int, stdin.readline().split())

h = [(0, n)]
visit = [False for _ in range(100003)]
visit[n] = True

while h:
    cnt, x = heappop(h)
    if x == k:
        print(cnt)
        exit()
        
    tmp = x*2
    while tmp < 100002 and not visit[tmp]:
        visit[x] = True
        heappush(h, (cnt, tmp))
        if tmp == k:
            print(cnt)
            exit()
        tmp *= 2
    
    if x < 100002 and not visit[x+1]:
        heappush(h, (cnt+1, x+1))
        visit[x+1] = True
    
    if x > 0 and not visit[x-1]:
        heappush(h, (cnt+1, x-1))
        visit[x-1] = True
        
print(-1)
    