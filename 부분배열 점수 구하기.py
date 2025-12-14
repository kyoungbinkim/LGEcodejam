from sys import stdin

p = 10**9 + 7

def calcScore(idx, n):
    if n == 0:
        return 0
    if idx  == 1:
        return 1 * n

    return idx**2 * (pow(idx, n, p) - 1) * pow(idx-1, p-2, p) % p
    

def solve():
    n = int(stdin.readline())
    nums = [None] + list(map(int, stdin.readline().split()))
    vis = set()
    
    
    start, end = 1, 1
    ans = 0
    for i in range(1, n+1):
        
        if len(vis) == 0:
            vis.add(nums[i])
            start = i
            end = i 
        elif nums[i] not in vis:
            vis.add(nums[i])
            end = i
        elif nums[i] in vis:
            
            length = end - start 
            for j, idx in enumerate(range(start, end+1)):
                # print(idx, length-j, j , calcScore(idx, length - j), calcScore(idx, j))
                ans += calcScore(idx, length - j)
                ans += calcScore(idx, j)
                ans %= p
            
            before = [start, end]
            while  nums[i] != nums[start]:
                vis.remove(nums[start])
                start += 1
            start += 1
            end = i
            
            if start < before[1]:
                length = before[1] - start 
                for j , idx in enumerate(range(start, before[1]+1)):
                    # print("minus : ", calcScore(idx, length - j), calcScore(idx, j))
                    ans -= calcScore(idx, length - j)
                    ans -= calcScore(idx, j)
                    ans %= p
                    
            
        # print("start : ", start, "end : ", end, "ans : ", ans, '  vis : ', vis)
    
    length = end - start 
    for j, idx in enumerate(range(start, end+1)):
        # print(idx, length-j, j , calcScore(idx, length - j), calcScore(idx, j))
        ans += calcScore(idx, length - j)
        ans += calcScore(idx, j)
        ans %= p
        
    # print('ans : ', ans, '\n')
    print(ans)

for _ in range(int(stdin.readline())):
    solve()