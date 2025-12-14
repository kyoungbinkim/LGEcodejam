from sys import stdin

ans = 0
n,m = map(int, stdin.readline().split())
maxlen = min(n,m)//2+1  if min(n,m)%2 else min(n,m)//2-1

b = [[int(x) for x in stdin.readline().strip()] for _ in range(n)]

dp = [[[0,0] if  b[0][i] == 0 else [1,1] for i in range(m)] if j ==0 else 
     [[0,0] for _ in range(m)] for j in range(n)]

for i in range(1, n):
    for j in range(m):
        if j-1 >= 0 and b[i][j] == 1:
            dp[i][j][0] = dp[i-1][j-1][0] + 1
        elif j-1 < 0 and b[i][j] == 1:
            dp[i][j][0] = 1
        
        if j+1 < m and b[i][j] == 1:
            dp[i][j][1] = dp[i-1][j+1][1] + 1
        elif j+1 >= m and b[i][j] == 1:
            dp[i][j][1] = 1
    

for i in range(n-1, -1, -1):
    for j in range(m):
        l = min(dp[i][j])
        
        if l < ans:
            continue
        
        for k in range(l-1, ans-1, -1):
            if i-k < 0 :
                continue
            if j-k >= 0 and dp[i-k][j-k][1]  > k and j+k < m and dp[i-k][j+k][0] > k:
                ans = k+1
                break

print(ans)


'''
10 7
0100010
0010100
0001000
1010101
0100010
1010101
0001000
0010100
0100010
0000010


10 10
0000100000
0001010000
0010101000
0101010100
1010101010
0101010001
0010101010
0001010100
0000101000
0000010000

'''