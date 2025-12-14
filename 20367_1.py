from sys import stdin


n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

# from random import randint
# n = randint(3,11)
# a = [randint(1,10) for _ in range(n)]
# print(a)


if n == 2:
    print(a[0] * a[1])
    exit()

dp = [0 for _ in range(n)]

dp[0] = a[1] * a[2]
dp[1] = a[0] * a[2]
dp[2] = a[0] * a[1]

for i in range(3, n, 2):
    if i == n-1:
        for j in range(i):
            dp[j] += a[j] * a[i]
        break
    
    temp = [0,0]
    area = a[i] * a[i+1]
    for j in range(i):
        for k in range(2):
            temp[k] = max(temp[k], a[i+1-k] * a[j] + dp[j])
        dp[j] += area
        
    dp[i] = temp[0]
    dp[i+1]=temp[1]
    # print(f"""
    #       dp[{i}] = {dp[i]}
    #       dp[{i+1}] ={dp[i+1]}
    #       {dp}
    #       """)

# print(dp)
print(max(dp))