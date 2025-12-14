from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    
    for i in range(n-1):
        a[i+1] -= a[i]-1
        if a[i] < 1:
            a[-1] += 100
            break
    
    if 0 <= a[-1] <=1:
        print("YES")
    else:
        print("NO")

