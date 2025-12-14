from sys import stdin

n, k= map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))

dp = [False for _ in range(k+1)]

for i in range(1, k+1):

    tmp = False
    for d in dp:
        if d>i:
            break
        dp[i]