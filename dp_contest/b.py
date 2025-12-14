from sys import stdin

n, k = map(int, stdin.readline().split())
h = list(map(int, stdin.readline().split()))

cost = [float('inf') if i != 0 else 0 for i in range(n)]

for i in range(1, n):
    
    for j in range(1, k+1):
        if j > i:
            break
        cost[i] = min(
            cost[i],
            cost[i-j] + abs(h[i] - h[i-j])
            )
print(cost[-1])
        