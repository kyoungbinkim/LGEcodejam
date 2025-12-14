from sys import stdin

import random

n = random.randint(5, 20)
# n = 1
a = 0
# a = random.randint(0, 10)
# b = random.randint(a, 11)
b=a
m = random.randint(10, 120)
m = 0

s = []
for _ in range(n):
    __s = random.randint(1, 100)
    s.append([__s, random.randint(1, 1+__s//3)])
s = sorted(s)
print(s, f"a:{a}, b:{b}, m:{m}")

# n, a, b, m = map(int, stdin.readline().split())

# s = sorted([list(map(int, stdin.readline().split())) for _ in range(n)])

day, wknd, work, ovr = 0, 0, 0, 0
cnt = 0
for i, (d,t) in enumerate(s):
    day = d//7 * 5 +  (5 if d%7 == 6 else d%7) 
    wknd = d//7 * 2  + (d%7 // 6) 
    print()
    print(d)
    print(day, wknd)
    print(f"work: {work}, ovr:{ovr}, total : {sum([tmp[1] for tmp in s[:i+1]])}")
    work += t
    
    if work > day:
        ovr += work-day
        work = day
    
    if ovr > d:
        print(-1)
        exit()
    elif ovr > day:
        cnt += ovr - day
        ovr = day

ans = -1
if a==0 and b ==0:
    if m>0:
        pass  
    elif ovr > s[-1][0]:
        pass
    else:
        ans = max(ovr - day, 0)
    print("sum : ", sum([tmp[1] for tmp in s]) , day * 2)
    print("cnt :", cnt)

elif a==0:
    if m % b:
        pass
    elif m//b <= wknd:
        ans = m//b

elif b == 0:
    if m % a == 0 and ovr : 
        if m//a <= day  and  ovr - m // a <= wknd:
            ans = max(ovr - m // a, 0)
else:
    for _y in range(wknd+1): 
        ax = m - _y * b
        
        if ax >= 0 and ax % a == 0 and ax // a <= day and \
            s[-1][0] >= ax // a + _y >= ovr:
            # print(f"a : {(m - _y * b )//a}")
            ans = _y
            break
        # for _x in range(day+1):
        #     if _x+_y > work+day:
        #         break
        #     if _x > day:
        #         break
        #     print(f"x:{_x} a:{a},  y:{_y} b:{b} m:{m}")
            
            
        #     if (m - _y * b ) % a == 0 and (m - _y * b ) // a <= day:
        #         ans = _y
        #         break
            
        #     # if _x * a + _y * b == m:
        #     #     ans = _y
        #     #     break
        # if ans>= 0:
        #     break

print(ans)

# print(f"( m - b * wknd ) / a : {( m - b * wknd ) / a}")
# print(f"x")
# print(f"day : {day}")

'''

ax + by = m
n>= x+y >= ovr
day >= x
wknd >= y

y = (m-ax) / b
b * wknd >= (m-ax) 
ax >=m - b * wknd
x >= ( m - b * wknd ) / a

'''