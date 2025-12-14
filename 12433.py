from sys import stdin

p = 32749

def comb(n, r):
    if r <= 0 or n < r:
        return 0
    
    if n//2 < r:
        r = n - r
    
    ans = 1
    for i in range(n, n-r, -1):
        ans *= i
        ans %= p
    
    for i in range(2, r+1):
        ans *= pow(i, p-2, p)
        ans %= p
    return ans
    
def sol(t):
    b,w,k,i = map(int, stdin.readline().split())    
    ans = 0
    
    if b == 0 or w == 0:
        if i == 1:
            ans = 1
    elif b+w == k:
        if i == 1:
            ans = comb(k-1, b)
            ans += comb(k-1, w)
    else:
        if i == 1:
            ans += comb(k-1, b)
            ans += comb(k-1, w)
        else:
            ans += comb(k-i, w-i+1)
            ans += comb(k-i, b-i+1)    
    print("Case #%d: %d" % (t+1, ans))

for t in range(int(stdin.readline())):
    sol(t)

# b b b b b w w w w

# b  w  w  b  b  b


