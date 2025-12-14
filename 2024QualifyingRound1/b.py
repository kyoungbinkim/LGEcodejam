from sys import stdin

t= int(stdin.readline())

#dp
for _ in range(t):

    n, b, c = map(int, stdin.readline().split())
    p = list(map(int, stdin.readline().split()))
    f = list(map(int, stdin.readline().split()))
    d = list(map(int, stdin.readline().split()))    
    
    costs = [float('inf') for _  in range(c+1)]
    costs[b] = 0

    for i in range(n):
        next = [float('inf') for _ in range(c+1)]

        for battery, cost in enumerate(costs):
            if cost == float('inf'):
                continue
            
            # 사용
            if battery >= d[i]:
                next[battery - d[i]] = min(
                    next[battery - d[i]],
                    cost
                )

            # 충전
            next[battery + p[i] if battery + p[i] <= c else c] = min(
                next[battery + p[i] if battery + p[i] <= c else c],
                cost + f[i] * d[i]
            )

        costs = next
    print(min(costs[b:]))