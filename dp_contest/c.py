from sys import stdin
n = int(stdin.readline())
h = [0,0,0]

for _ in range(n):
    tmp = [0, 0, 0]
    v = list(map(int, stdin.readline().split()))
    
    for i in range(3):
        tmp[i] = max(
            h[i-1] + v[i],
            h[i-2] + v[i]
        )
    h = tmp
print(max(h))