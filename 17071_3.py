from sys import stdin
from collections import deque

n ,k = map(int, stdin.readline().split())

dp = [-1 for _ in range(500_001)]
dp[n] = 0
q = deque([(n, 0)])

while q:
    next, cnt = q.popleft()
    
    if next -1 >= 0  and dp[next-1] < 0:
        q.append((next-1, cnt+1))
        dp[next-1] = cnt+1
    
    if  next + 1 <= 500_000 and dp[next+1] < 0:
        q.append((next+1, cnt+1))
        dp[next+1] = cnt+1
        
    if  next * 2 <= 500_000 and dp[next * 2] < 0:
        dp[next * 2] = cnt +1
        q.append((next*2, cnt+1))

diff = 0


while k <= 500_000:
    print(k, dp[k] ,diff)
    if dp[k] < diff :
        if n>k and (diff-dp[k]) % 2 ==0:
            break
            
    elif dp[k] == diff:
        break
    
    diff += 1
    k += diff
    
print(diff if k<=500_000 else -1)