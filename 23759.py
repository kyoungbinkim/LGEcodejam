from sys import stdin

def sol():
    n,k = map(int,stdin.readline().split())
    strs = [stdin.readline().strip() for _ in range(n)]
    close = [[-1 for _ in range(26)] for _ in range(k)] # idx
    
    dp = []
    for i in range(n):
        dp.append(float('inf'))
        for j,c in enumerate(strs[i]):
            if close[j][ord(c)-ord('a')] == -1:
                dp[i] = min(dp[i], i)
                close[j][ord(c)-ord('a')] = i
                continue
            dp[i] = min(dp[i],  dp[close[j][ord(c)-ord('a')]] + i - close[j][ord(c)-ord('a')] - 1)
            close[j][ord(c)-ord('a')] = i
    
    # print(dp)
    print(min([n-1-i+dp[i] for i in range(n)]))
sol()