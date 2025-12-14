from sys import stdin
from collections import deque

rl = stdin.readline

n,m,t = map(int, rl().split())
built = set(map(int, rl().split()))

infos = [[], ]
for idx in range(n):
    info = list(map(int, rl().split()))
    infos.append(info[1:])

linked = [set() for _ in range(n+1)]
deg = [0 for _ in range(n+1)]

for _ in range(n-m):
    d = list(map(int, rl().split()))
    
    deg[d[0]] = len(d)-2
    
    for start in d[2:]:
        linked[start].add(d[0])

# print("built", built)
# print("infos", infos)
# print("linked", linked)
# print("deg", deg)

q = deque([(idx, 0) for idx in built])
while q:
    idx, time = q.popleft()
    if time >= t:
        break
    built.add(idx)
    
    for i in infos[idx]:
        # print("i", i, infos[idx], linked[i])
        # if i in built:
        #     continue 
        for j in linked[i]:
            if j in built or deg[j] == 0:
                continue
            deg[j] -= 1
            if deg[j] == 0:
                q.append((j, time+1))
    print(idx, time, built)
    print(deg, "\n")

print(len(built) )
print(*sorted(built))