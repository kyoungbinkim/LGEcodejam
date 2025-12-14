from sys import stdin

def test_input(n=3000):
    import random
    s = [chr(random.randint(97, 122)) for _ in range(n)]
    t = [chr(random.randint(97, 122)) for _ in range(n)]
    return s, t
# s,t = test_input(30)

s = [c for c in stdin.readline().rstrip('\n')]
t = [c for c in stdin.readline().rstrip('\n')]


dp = [['' for _ in range(len(t)+1)] for _ in range(len(s) + 1)]

def debug_dp():
    for dd in dp:
        print(dd)

x,y = 1,1

for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + s[i-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)

print(dp[-1][-1])