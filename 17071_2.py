from sys import stdin
import random

def countOne(d:list, c):
    cnt = 0
    
    def _count(d:list):
        cnt = 0
        flag = 0
        for i in d:
            if i == '0':
                cnt += flag if flag <= 1 else 2
                flag = 0
            else:
                flag += 1
        cnt += flag if flag <= 1 else 2
        return cnt
    
    if len(d) < c:
        cnt += d.count('1')
    else:
        cnt += d[-c-1:].count('1')    
        if c == 8 or c == 9:
            print(f"cnt : {cnt}, c: {c}")
            print(f"{d[:-c-1]} {d[-c-1:]}")
        for i,b in enumerate(d[:-c-1][::-1]):
            cnt += int(b) * (2**(i+1))
    return cnt

# 
# for _ in range(5):
#     n,k = random.randint(0, 500000), random.randint(0, 500000)
    
#     diff = [ c if c!='b' else '0' for c in bin(n- k)[2:]]
#     c = random.randint(1, 10)
#     cnt = countOne(diff, c)
#     print(f'''
#           n : {bin(n)}
#           k : {bin(k)}
#           n-k : {bin(n-k)}
#           c : {c}
#           cnt : {cnt}
#           ''')
    

def check(n, k, steps):
    print(bin(n))
    print(bin(k))
    _n = n
    c = 0
    square = 1
    while c <= steps and _n <= 500_000:
        if abs(k - _n) > 500_000:
            c += 1
            square *= 2
            _n *= 2
            continue
        diff = [ c if c!='b' else '0' for c in bin(k - _n)[2:]]
        
        cnt = countOne(diff, c)
        print(f'cnt : {cnt}, steps:{steps}, c:{c}, k : {k}, _n : {_n}, k-n : {k-_n}')
        if cnt <= steps - c:
            print(f"f{diff}")
            print(f"{diff[:-c-1]} {diff[-c-1:]}")
            return True
        
        c += 1
        square *= 2
        _n *= 2
    return False

n,k = map(int, stdin.readline().split())
# n,k = random.randint(0, 500000), random.randint(0, 500000)
step = 0

while k <= 500_000:
    
    # print(f'''
    #       n : {n}
    #       k : {k}
    #       ''')
    if check(n,k,step):
        break
    
    step += 1
    k += step

print(bin(n+410))
print(bin(k), step)
print(bin(k - (n+410) * 16))
print(step if k <= 500_000 else -1)


'''
0b1000001010
0b100000101010001110 96
'''