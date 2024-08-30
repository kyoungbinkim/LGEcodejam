from sys import stdin
from collections import deque

def solve():
    n = int(stdin.readline())
    nums = [[int(x), idx, 1, idx] for idx, x in enumerate(stdin.readline().split())]
    
    ans = 0
    stck = deque([nums[0]])
    # print(nums)
    for i in range(1, n):
        if len(stck) == 0:
            stck.append(nums[i])
            continue
        
        if len(stck) and stck[-1][0] > nums[i][0]:
            ans += nums[i][1] * stck[-1][2] - stck[-1][3]  + stck[-1][2]
            
            if abs(stck[-1][1] - nums[i][1]) ==1:
                ans -= 2
            stck.append(nums[i])

            continue    
        

        while len(stck) and stck[-1][0] < nums[i][0]:
            tmp = stck.pop()
            
            ans += nums[i][1] * tmp[2] - tmp[3] + tmp[2]
            if nums[i][1] - tmp[1] == 1:
                ans -= 2
        
        if len(stck) and stck[-1][0] == nums[i][0]:
            
            ans += nums[i][1] * stck[-1][2] - stck[-1][3]  + stck[-1][2]
            if abs(stck[-1][1] - nums[i][1]) ==1:
                ans -= 2
            
            stck[-1][1] = nums[i][1]
            stck[-1][2] += 1
            stck[-1][3] += nums[i][1]
            
            if len(stck) > 1:
                ans += nums[i][1] * stck[-2][2] - stck[-2][3]  + stck[-2][2]
        elif len(stck):
            ans += nums[i][1] * stck[-1][2] - stck[-1][3]  + stck[-1][2]
            if abs(stck[-1][1] - nums[i][1] )==1:
                ans -= 2
            stck.append(nums[i])
        else:
            stck.append(nums[i])
            
            
        print(nums[i], stck, ans)  
    print('\n', ans, '\n\n')
    print(ans)

for _ in range(int(stdin.readline())):
    solve()