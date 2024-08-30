from sys import stdin
from itertools import combinations

p = 1_000_000_007
n = int(stdin.readline())
(nums := list(map(int, stdin.readline().split()))).sort()
# print(*nums)
ans = 0
for i in range(n):
    ans += p - (nums[i] * (pow(2, n-i-1,p) - 1)) % p
    ans += (nums[i] * (pow(2, i, p) - 1)) % p
    ans %= p
print(ans % p)