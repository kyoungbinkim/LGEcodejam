from sys import stdin

rl = stdin.readline

def parseK(k):
    parsed = []
    if k <= 11:
        tmp = [6,3,1,1]
        idx = 3
        
        while k >= tmp[idx]:
            k -= tmp[idx]
            parsed.append(tmp[idx])
            idx -= 1
        if k > 0:
            parsed.append(k)
    else:
        parsed.append(1)
        k -= 1
        
        while k >= parsed[-1] * 2:
            k -= parsed[-1] * 2
            parsed.append(parsed[-1] * 2)
        if k:
            parsed += parseK(k)
    return parsed


n, m = map(int, rl().split())
goods = []
for _ in range(n):
    v,c,k = map(int, rl().split())
    pk = parseK(k)
    
    for p in pk:
        goods.append((v*p, c*p))


l = len(goods)
dp =[ [0 for _ in range(m+1)] for _ in range(l+1)]

for i in range(1, l+1):
    for w in range(1, m+1):
        if goods[i - 1][0] <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - goods[i - 1][0]] + goods[i - 1][1])
        else:
            dp[i][w] = dp[i - 1][w] 

print(dp[-1][-1])
