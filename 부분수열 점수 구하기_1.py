from sys import stdin


p = 10**9 + 7

def calcScore(idx, n):
    if n == 0:
        return 0
    if idx  == 1:
        return 1 * n

    return idx**2 * (pow(idx, n, p) - 1) * pow(idx-1, p-2, p) % p



def solve():
    n = int(stdin.readline())
    nums = [None] + list(map(int, stdin.readline().split()))
    ans = 0
    for i in range(1, n):
        vis = set([nums[i]])
        for j in range(i+1, n+1):
            if nums[j] in vis:
                break
            else:
                ans += pow(i, j-i+1, p)
                ans += pow(j, j-i+1, p)
                ans %= p
                vis.add(nums[j])
        print("ans : ", ans)
    print(ans)

for _ in range(int(stdin.readline())):
    solve()