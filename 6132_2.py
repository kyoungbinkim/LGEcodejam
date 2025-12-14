from sys import stdin

n,c = map(int, stdin.readline().split())

scores = [[abs(i-j)*c for j in range(101) ] for i in range(101)]
double = [i**2 for i in range(101)]
# hi = [int(stdin.readline()) for _ in range(n)]

dp = []

for _ in range(n):
    h = int(stdin.readline())
    # print(dp)
    
    if len(dp) == 0:
        dp = [[i, (i-h) **2] for i in range(h, 101)]
        continue
    
    update = []
    
    for i in range(h, 101):
        tmp = [i, float('inf')]
        diff = double[i-h]
        for d, v in dp:
            tmp[1] = min(tmp[1], v+scores[d][i] + diff)    
        update.append(tmp)
    dp = update
print(min([d[1] for d in dp]))