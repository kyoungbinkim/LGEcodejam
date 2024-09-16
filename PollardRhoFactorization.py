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