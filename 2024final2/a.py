from sys import stdin
from bisect import bisect_left

rl = stdin.readline

winMap = {
    'A' : 0,
    'B' : 1,
}

        
def sol():
    ans = 0
    n, m = map(int, rl().split())
    Aacc,Bacc = [0], [0]
    w = rl().strip()
    
    for i , c in enumerate(w * 2):
        Aacc.append(Aacc[-1])
        Bacc.append(Bacc[-1])
        if c == 'A':
            Aacc[-1] += 1
        else:
            Bacc[-1] += 1


    for _ in range(m):
        s, g = map(int, rl().split())
        tar = (g+1) // 2
        if Aacc[s+g-1] - Aacc[s-1] >= tar:
            tmp = bisect_left(Aacc, Aacc[s-1] + tar, lo=s, hi= s+g-1)
        else:
            tmp = bisect_left(Bacc, Bacc[s-1] + tar, lo=s, hi= s+g-1)
        ans += tmp - s + 1
        
    return ans

for _ in range(int(rl())):
    print(sol())