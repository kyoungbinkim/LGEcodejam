from sys import stdin

n, w = map(int, stdin.readline().split())

jew = [list(map(int, stdin.readline().split())) for _ in range(n)] # w, v
candidate = [0]
w2i, i2w,idx = {0:0}, {0:0}, 0


for _w, _v in jew:
    tmp = []
    for c in candidate:
        if _w+c > w:
            continue
        tmp.append(_w+c)
    candidate += tmp
candidate.sort()

w2i = {v:i for i,v in enumerate(candidate)}
i2w = {i:v for i,v in enumerate(candidate)}

dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(w+1):
        print(f"""
              i {i}
              j : {j}
              jew[i-1] : {jew[i-1]}
              i2w[j] : {i2w[j]}
              """)
        dp[i][j] = dp[i-1][j] if i2w[j]<jew[i-1][0] else  max(
            dp[i - 1][j], 
            dp[i - 1][ w2i[i2w[j] - jew[i-1][0]] ] + jew[i - 1][1]
        )

    print(dp)