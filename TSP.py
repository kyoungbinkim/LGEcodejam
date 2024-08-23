from sys import stdin

global b, n, dp

def TSP(i, visit):
    global b, n, dp
    
    if visit == (1<<n)-1:
        return b[i][0] if b[i][0] > 0 else float('inf')
    
    if dp[i][visit] != -1:
        return dp[i][visit]
    
    dp[i][visit] = float('inf')
    for j in range(n):
        if visit & (1<<j) == 0 and b[i][j] > 0:
            dp[i][visit] = min(dp[i][visit], TSP(j, visit | (1<<j)) + b[i][j])
    return dp[i][visit]
    
def sol():
    global b, n, dp
    
    n = int(stdin.readline())
    b = [list(map(int, stdin.readline().split())) for _ in range(n)]
    dp = [[-1 for _ in range(2**n)] for _ in range(n)]
    
    ans = TSP(0, 1)
    print(ans)    
    

sol()
    
    
    