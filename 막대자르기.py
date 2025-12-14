from sys import stdin

def solve():
    n,k,a,b = map(int, stdin.readline().split())

    s=[(a*(x-1)**2+b, x) if x!= 1 else (0,1)   for x in map(int, stdin.readline().split())]
    
    dp = [float('inf') for _ in range(k+1)]
    
    s.sort(key=lambda x: x[1])
    # print(s)
    # visit = set()
    for i in range(n):
        tmp = s[i]
        if tmp[1] > k:
            dp[k] = min(dp[k], tmp[0])
            continue
       
        update = set()
        
        for j in range(k, 0, -1):
            if dp[j] == float('inf'):
                continue
            if j + tmp[1] <= k:
                dp[j+tmp[1]] = min(dp[j+tmp[1]], dp[j] + tmp[0])
            else:
                dp[k] = min(dp[k], dp[j] + tmp[0])
        dp[tmp[1]] = min(dp[tmp[1]], tmp[0])
    #     print(tmp, dp)    
    # print(dp)
    print(dp[-1])

for _ in range(int(stdin.readline())):
    solve()