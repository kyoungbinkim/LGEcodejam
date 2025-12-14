from sys import stdin
from collections import deque

rl = stdin.readline


n,m,t = map(int, rl().split())
built = set(map(int, rl().split()))
canBuild = set()
infos = [[], ]
for idx in range(n):
    info = list(map(int, rl().split()))
    infos.append(info[1:])
    if idx+1 in built:
        canBuild.update(info[1:])


q = deque()
deg = [set() for _ in range(n+1)]
link = [set() for _ in range(n+1)]
for _ in range(n-m):
    d = list(map(int, rl().split()))
    deg[d[0]] = set(d[2:]).difference(canBuild)
    if len(deg[d[0]]) == 0:
        q.append((d[0], 0))
    
    for start in d[2:]:
        link[start].add(d[0])

# print("built", built)
# print("canBuild", canBuild)
# print("infos", infos)
# print("deg", deg)
# print("link", link)

while q:
    
    idx, time = q.popleft()
    if time >= t:
        break
    canBuild.add(idx)
    
    for i in infos[idx]:
        for delete in link[i]:
            
            deg[delete]-={i}
            if len(deg[delete]) == 0 and delete not in canBuild:
                q.append((delete, time+1))
                
canBuild= list(canBuild.union(built))
print(len(canBuild))
print(" ".join(map(str, sorted(canBuild))))

