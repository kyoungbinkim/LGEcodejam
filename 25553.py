from sys import stdin
from collections import deque
from math import ceil, floor

n, q, k = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

cnt = [ceil(k/2), floor(k/2)] # 홀 짝
maps, update = { }, [0, 0] # 홀 짝

s = sum(nums[:k])
deq = deque(nums[:k])
maps[tuple(cnt)] = (s, 1)

sIdx , eIdx = 1, k

for num in nums[k:] + nums[:k]:
    deq.append(num)
    s += num
    s -= deq.popleft()

    eIdx = eIdx%n + 1
    cnt[1 - sIdx%2] -= 1
    cnt[1 - eIdx%2] += 1
    sIdx = sIdx%n + 1
    
    if s > maps.get(tuple(cnt), (-float('inf'), -1))[0]:
        maps[tuple(cnt)] = (s, sIdx)
    

for _ in range(q):
    cmd = list(map(int, stdin.readline().split()))
    if cmd[0] == 1:
        update[0] += cmd[1]
    elif cmd[0] == 2:
        update[1] += cmd[1]
    elif cmd[0] == 3:
        ans =( -float('inf'), 0)
        for k in maps.keys():
            tmp = 0
            for i in range(2):
                tmp += k[i] * update[i]
            if ans[0] < tmp + maps[k][0]:
                ans = (tmp + maps[k][0], maps[k][1])
        print(ans[1], ans[0])
        

# print(maps)

# 5 3 3
# 2 -5 3 -4 9

# 8 3 4
# 2 -5 3 -4 9 3 10 100

'''
9 3 6
2 -5 3 -4 9 3 10 100 90
3
2 10
3
'''