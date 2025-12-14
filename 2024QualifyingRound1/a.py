from sys import stdin
from math import ceil

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())

    d = list(map(int, stdin.readline().split()))
    s = stdin.readline().rstrip()
    r = list(map(int, stdin.readline().split()))
    a, b = 1, 0
    ans = d[-1] + 1

    # a X  > b
    for dd, dr, ds  in zip(d[:-1][::-1], r[:-1][::-1], s[:-1][::-1]):

        if ds == '+':
            ans -= dr
            ans = max(ans, 1)
        else:
            ans /= dr
        ans += dd

    print(ceil(ans))