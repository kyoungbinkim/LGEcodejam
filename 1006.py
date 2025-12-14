from sys import stdin

rl = stdin.readline 

def sol():
    n, w = map(int, rl().split())
    r = [list(map(int, rl().split())) for _ in range(2)]
    
    def dynamicPrograming(r, n, flag = False):
        dp = [[0 for _ in range(4)] for _ in range(n)]
        # if flag:
        #     dp[0] = [0, 1, 1, 2]
        # else:
        #     dp[0] = [0, 1, 1, 1 if r[0][0] + r[1][0] <=w else 2]
        dp[0] = [0, 1, 1, 1 if r[0][0] + r[1][0] <=w else 2]   
        
        for idx in range(n-1):
            
            dp[idx+1][0] = min(dp[idx][1] + 1 , dp[idx][2] + 1, dp[idx][3])

            tmp = [dp[idx][3] + 1, dp[idx][1] + 2, dp[idx][0] + 3, dp[idx][2] + 2]
            if r[0][idx] + r[0][idx+1] <= w:
                tmp.append(dp[idx][2] + 1)
                tmp.append(dp[idx][0] + 2) 
            dp[idx+1][1] = min(tmp)
            
            tmp = [dp[idx][0] +3, dp[idx][1] + 2, dp[idx][2] + 2, dp[idx][3] + 1]
            if r[1][idx] + r[1][idx+1] <= w:
                tmp.append(dp[idx][1] + 1)
                tmp.append(dp[idx][0] + 2)
            dp[idx+1][2] = min(tmp)
            
            tmp = [dp[idx][0] + 4, dp[idx][1] + 3, dp[idx][2] + 3, dp[idx][3] + 2]
            if r[0][idx+1] + r[1][idx+1] <= w:
                tmp.append(dp[idx][3] + 1)
                tmp.append(dp[idx][1] + 2)
                tmp.append(dp[idx][2] + 2)
                tmp.append(dp[idx][0] + 3)
            
            if r[0][idx] + r[0][idx+1] <= w and r[1][idx] + r[1][idx+1] <= w:
                tmp.append(dp[idx][2] + 2)
                tmp.append(dp[idx][1] + 2)
                tmp.append(dp[idx][0] + 2)
            else:
                if r[0][idx] + r[0][idx+1] <= w:
                    tmp.append(dp[idx][0] + 3)
                    tmp.append(dp[idx][1] + 3)
                    tmp.append(dp[idx][2] + 2)
                
                elif r[1][idx] + r[1][idx+1] <= w:
                    tmp.append(dp[idx][0] + 3)
                    tmp.append(dp[idx][1] + 2)
                    tmp.append(dp[idx][2] + 3)
            dp[idx+1][3] = min(tmp)
        ans = dp[n-1][3]
        print(dp)
            
        if flag:
            return dp[n-1]
            # if r[0][0] + r[0][n-1] <= w and r[1][0] + r[1][n-1] <= w:
            #     ans = min(ans, dp[n-2][3])
            # if r[0][0] + r[0][n-1] <= w:
            #     ans = min(ans, dp[n-1][2])
            # if r[1][0] + r[1][n-1] <= w:
            #     ans = min(ans, dp[n-1][1])
        
        return ans
    
    
    ans = dynamicPrograming(r, n)
    if r[0][0] + r[0][n-1] <= w or r[1][0] + r[1][n-1] <= w:
        newR = [r[0][1:], r[1][1:]]
        tmp = dynamicPrograming(newR, n-1, True)
        if r[0][0] + r[0][n-1] <= w:
            ans = min(ans, tmp[2]+2)
        if r[1][0] + r[1][n-1] <= w:
            ans = min(ans, tmp[1]+2)
    if r[0][0] + r[0][n-1] <= w and r[1][0] + r[1][n-1] <= w:
        newR = [r[0][1:n-1], r[1][1:n-1]]
        tmp = dynamicPrograming(newR, n-2)
        ans = min(ans, tmp+2)

    
    # newR = []
    # newR.append(r[0][1:n-1])
    # newR.append(r[1][1:n-1])
    # print(len(newR[0]), n)
    
    # r[0].append(r[0].pop(0))
    # r[1].append(r[1].pop(0))
    # ans = min(ans, dynamicPrograming(r, n))
    # ans = min(ans, dynamicPrograming(r, n))
    
    
    # r[0].append(r[0].pop(0))
    # r[1].append(r[1].pop(0))
    # ans = min(ans, dynamicPrograming(r, n))
    
    print(ans)
    return ans

a = []
for _ in range(int(rl())):
    a.append(sol())
print(a)