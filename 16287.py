from sys import stdin
from collections import deque

w,n = map(int,stdin.readline().split())
nums = deque(map(lambda x: [set([int(x)]), set(), set()],stdin.readline().split()))
# print(nums)

def findAndUpdate(a, b):
    ret = [a[i].union(b[i]) for i in range(3)]
    for _a in a[1]:
        if w-_a in b[1]:
            print('YES')
            exit()
        for _b in b[0]:
            ret[2].add(_a+_b)
        
    for num in a[2]:
        if w-num in b[0]:
            print('YES')
            exit()
    for num in b[2]:
        if w-num in a[0]:
            print('YES')
            exit()
        
    for _a in a[0]:
        for _b in b[0]:
            ret[1].add(_a+_b)
        for _b in b[1]:
            ret[2].add(_a+_b)
            
    return ret

while len(nums) > 1:
    a = nums.popleft()
    b = nums.popleft()
    nums.append(findAndUpdate(a, b))
print('NO')