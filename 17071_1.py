from sys import stdin, setrecursionlimit
setrecursionlimit(10**4)

# n, k = map(int, stdin.readline().split())


import random
n,k = random.randint(0,500_000), random.randint(0,500_000)
print(n,k)

def _check(s, d):
    sbin,dbin = bin(s)[2:], bin(d)[2:]
    
    if len(sbin) > len(dbin):
        return -1
    
    for i in range(
        min(len(sbin), len(dbin))
    ):
        if sbin[i] != dbin[i]:
            return i
    
    return min(len(sbin), len(dbin))
    
    
def find_(s,d, cnt, depth):    
    if s == d:
        return depth - cnt
    
    if s > 500_000 or s<0 or d>500_000 or cnt >= depth or depth < 0:
        if s == d:
            return 0
        return -float('inf')
    
    
    checks = [
        _check(s-1,d), _check(s+1,d), _check(2*s,d)
    ]
    
    idx = checks.index(max(checks))
    if idx == 0:
        return find_(s-1, d, cnt+1, depth) + 1
    elif idx == 1:
        return find_(s+1, d, cnt+1, depth) + 1
    else:
        return find_(2*s, d, cnt+1, depth) + 1
     
is_find = n == k
dk = 0

while k <= 500_001 and not is_find:
    dk += 1
    k += dk
    
    if n > k:
        print(f"n : {n}, k : {k}")
        if dk == n - k:
            is_find = True
            break
        continue
    print(f"k-n : {k-n}, dk : {dk},   n:{n} k:{k}")
    # print(f" dk : {dk}")
    # print(f"print(dk) : {dk}, _find : {find_(n,k,0,dk)}")
    if (dk - find_(n,k,0,dk)) % 2 == 0:
        is_find = True
        break
    
    kmax = 2 ** (len(bin(k)) - 2)
    
    # print(f"\n kmax : {kmax} (kmax - k) : {(kmax - k)}")
    
    if  find_(n, kmax, 0, dk - abs(kmax - k)) == dk - abs(kmax - k):
        is_find = True
        break

print(bin(n))
print(bin(k))
print(dk if is_find else -1)