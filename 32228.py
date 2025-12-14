from sys import stdin
from math import floor, ceil

def isPrime(n):
    if n == 2:
        return True
    if n == 1 or n%2 == 0 or n<0:
        return False
    for i in range(3, floor(n**0.5)+2, 2):
        if n%i == 0:
            return False
    return True

def gcd(a,b):
    if a==0 or b==0:
        return a+b
    return gcd(b, a%b) if a>b else gcd(a, b%a)

def PollardRhoFactorization(n, _x=2, _y=2):
    x, y, d = _x, _y, 1
    while d == 1:
        x = (x*x+1)%n
        y = (y*y+1)%n
        y = (y*y+1)%n
        d = gcd(abs(x-y), n)
    if d==n:
       return -1
    if isPrime(d):
        return d
    return PollardRhoFactorization(d, _x=_x, _y=_y)

# print(PollardRhoFactorization(9*7*13*27*103*103, _x=3))
# print(PollardRhoFactorization(21, _x=3), PollardRhoFactorization(7))
# print(PollardRhoFactorization(1024 * (1027**3) * 182, _x=5, _y=3))
# # print(18273491 % 13)
# print(1027  % 13, 1027 // 13)

n,m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

factor = {}

ans = 0
_x,_y =2,2
while m > 1:
    while m%2 == 0:
        m //= 2
        factor[2] = factor.get(2, 0) + 1
        break
    
    if m == 1:
        break
    
    if isPrime(m):
        factor[m] = factor.get(m, 0) + 1
        break
    
    k = PollardRhoFactorization(m, _x=_x, _y=_y)

    if k > 0:
        if m % k:
            _x += 1
            continue
        
        while m%k == 0:
            factor[k] = factor.get(k, 0) + 1
            m //= k
        _x, _y = 2, 2
    elif _x == _y:
        _x += 3
    else:
        _y += 3
# print(factor)
ans = 1
for k in factor.keys():
    ans *= (k ** (factor[k]-1)) * (k-1)
print(ans)



