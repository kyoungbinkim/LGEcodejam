from sys import stdin,setrecursionlimit
setrecursionlimit(10**9)

def reidx(n, offset):
    if n > 0:
        return n+offset
    else:
        return -n

def tarjan(_n, _G):
    n = _n
    G = _G
    stack = []
    f = [False for _ in range(n+1)] # 완료 확인
    nodeId = [0 for _ in range(n+1)] # 노드의 인덱스
    Id = [1]
    
    sccs = []
    
    def dfs(idx):
        nodeId[idx] = Id[0]
        Id[0] += 1
        
        stack.append(idx)
        parent = nodeId[idx]
        
        for i in G[idx]:
            if nodeId[i] == 0:
                parent = min(parent, dfs(i))
            elif not f[i]:
                parent = min(parent, nodeId[i])
        
        if parent == nodeId[idx]:
            scc = []
            while True:
                t = stack.pop()
                scc.append(t)
                f[t] = True
                if t == idx:
                    break
            sccs.append(scc)
        
        return parent

    for i in range(1, n+1):
        if nodeId[i] == 0:
            dfs(i)    
    return sccs

n, m = map(int, stdin.readline().split())
g = [[] for _ in range(2*n+1)]

for _ in range(m):
    a,b = map(int, stdin.readline().split())
    g[reidx(-a,n)].append(reidx(b,n))
    g[reidx(-b,n)].append(reidx(a,n))

sccs = tarjan(2*n, g)
# print(sccs)
for scc in sccs:
    for i in scc:
        if i>n and i-n in scc:
            print(0)
            exit()
print(1)