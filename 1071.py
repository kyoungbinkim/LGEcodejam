from sys import stdin
from heapq import heapify, heappop, heappush

n = int(stdin.readline())
heapify(h := list(map(int, stdin.readline().split())))

ans, buf = [] , []

while h:
    x = heappop(h)
    if ans:
        if ans[-1][0] == x:
            ans[-1][1]+=1
            continue
    ans.append([x,1])


i = 0
while i < len(ans):
    if len(buf) == 0:
        buf.append(ans[i])
        i+=1
        continue
    
    if ans[i][1] == 0:
        i+=1
        continue
    elif i == len(ans)-1:
        buf.append(ans[i])
        break
    
    if ans[i][0] - buf[-1][0] == 1:
        buf.append([ans[i+1][0],1])
        buf.append(ans[i])
        ans[i+1][1] -= 1
        i += 1
        continue
    buf.append(ans[i])
    i += 1
    
    # print(buf)
if len(buf) > 1 and buf[-1][0] - buf[-2][0] == 1:
    buf[-1], buf[-2] = buf[-2], buf[-1]
# print(buf)

tmp = []
for x,c in buf:
    tmp.extend([x]*c)
print(*tmp)