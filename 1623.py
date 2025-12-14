from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def sol():
    n = int(stdin.readline())
    vals = [0] + list(map(int,stdin.readline().split()))
    g = [[] for _ in range(n+1)]

    p = [-1, -1] + list(map(int,stdin.readline().split()))
    
    for i in range(2, n+1):
        g[p[i]].append(i)
    
    dp = [[[None, []], [None, []]] for _ in range(n+1)]
    
    def makeDP(idx):
        if dp[idx][0][0] != None:
            return dp[idx]

        if g[idx] == []:
            dp[idx][0] = [0, []]
            dp[idx][1] = [vals[idx], [idx]]
            return dp[idx]
        
        dp[idx] = [
            [0, []],
            [vals[idx], [idx]]
        ]
        
        for c in g[idx]:
            child = makeDP(c)
            
            dp[idx][0][0] += max([child[0][0], child[1][0], 0])
            dp[idx][1][0] += max([child[0][0], 0])
            
            if child[1][0] > 0:
                dp[idx][1][1] += child[0][1]
            
            if child[0][0] < 0 and child[1][0] < 0:
                pass
            elif child[0][0] > child[1][0]:
                dp[idx][0][1] += child[0][1]
            elif child[0][0] < child[1][0]:
                dp[idx][0][1] += child[1][1]
            dp[c] = None
        return dp[idx]
        
    
    # def dynamincPrograming(idx, visit=1):
    #     if dp[idx][visit][0] != None:
    #         return dp[idx][visit]
        
    #     if g[idx] == []:
    #         dp[idx][visit][0] = vals[idx] if visit else 0
    #         if visit:
    #             dp[idx][visit][1] = [idx]
    #         return dp[idx][visit]
        
    #     if visit == 0:
    #         dp[idx][visit][0] = 0
    #         for i in g[idx]:
    #             tmp = [
    #                 dynamincPrograming(i, 0),
    #                 dynamincPrograming(i, 1)
    #             ]
    #             if tmp[0][0] < 0 and tmp[1][0] < 0:
    #                 continue 
    #             selector = 0 if tmp[0][0] > tmp[1][0] else 1
                
    #             dp[idx][visit][0] += tmp[selector][0]
    #             dp[idx][visit][1] += tmp[selector][1]
                
    #     else:
    #         dp[idx][visit][0] = vals[idx]
    #         dp[idx][visit][1] = [idx]
    #         for i in g[idx]:
    #             tmp = dynamincPrograming(i, 0)
    #             if tmp[0] > 0:
    #                 dp[idx][visit][0] += tmp[0]
    #                 dp[idx][visit][1] += tmp[1]
    #             dp[i] == None
    #     return dp[idx][visit]
    
    makeDP(1)
    print(*[dp[1][1][0], dp[1][0][0]])
    print(*(sorted(dp[1][1][1]) + [-1]))
    print(*(sorted(dp[1][0][1]) + [-1]))

sol()
