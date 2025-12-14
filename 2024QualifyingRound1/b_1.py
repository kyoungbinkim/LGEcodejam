from sys import stdin

t= int(stdin.readline())

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
            # print(battery, d[i])
            if battery >= d[i]:
                # next[battery - d[i]] = min(
                #     next[battery - d[i]] if next[battery - d[i]] != None else float('inf'),
                #     cost
                # )
                next[battery - d[i]] = min(
                    next[battery - d[i]],
                    cost
                )
            
            # next[battery + p[i] if battery + p[i] <= c else c] = min(
            #     next[battery + p[i] if battery + p[i] <= c else c] if next[battery + p[i] if battery + p[i] <= c else c] != None else float('inf'),
            #     cost + f[i] * d[i]
            # )
            next[battery + p[i] if battery + p[i] <= c else c] = min(
                next[battery + p[i] if battery + p[i] <= c else c],
                cost + f[i] * d[i]
            )

        # print(next)
        costs = next
    print(min(costs[b:]))