from sys import stdin


# n = int(stdin.readline())
# a = list(map(int, stdin.readline().split()))

# if n == 2:
#     print(a[0] * a[1])
#     exit()
    
from random import randint
n = randint(3,11)
a = [randint(1,10) for _ in range(n)]

dp = [[[0,0]for _ in range(3)] for _ in range((n-2)//2 + 1)] # max val, remain


stcks = a[:3]
for i in range(3):
    dp[0][i] = [stcks[i-1] * stcks[i-2], stcks[i]]

print(a, '\n', stcks)
print(dp[0], dp)

for i in range(1, (n-2)//2 + 1):
    if i*2+1 == n-1:
        for j in range(3):
            dp[i][j] =[ dp[i-1][j][0] + dp[i-1][j][1]*a[i*2+1], 0]
        break
        
    
    # stck selector
    for j in range(3):
         
        # dp selector
        for k in range(3):
            
            if j != 2:
                calc_sum = dp[i-1][k][0] + dp[i-1][k][1] * a[i*2+2-j]  
            else:
                calc_sum = dp[i-1][k][0] + a[i*2+1] * a[i*2+2]
            
            if calc_sum > dp[i][j][0]:
                dp[i][j] = [calc_sum , a[i*2+1+j]] if j != 2 else [calc_sum, dp[i-1][k][1]]
    
    print(f"""
          i : {i}
          dp[i] : {dp[i]}
          """)

print(max([_dp[0] for _dp in dp[-1]]))
            

        
        