from sys import stdin
import sys
sys.setrecursionlimit(10**9)

rl = stdin.readline

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

for _ in range(int(rl())):
    n, m = map(int, rl().split()) # 도미노 수 , 엣지 수
    _g = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, rl().split())
        _g[a].append(b)
    
    scc = tarjan(n, _g)
    idx2scc = [0 for _ in range(n+1)]
    
    for i in range(len(scc)):
        for j in scc[i]:
            idx2scc[j] = i
    
    
    # print('--- updatae SCC graph ---')
    deg = [0 for _ in range(len(scc))]
    for i in range(1, n+1):
        for j in _g[i]:
            if idx2scc[i] != idx2scc[j]:
                deg[idx2scc[j]] += 1

    
    # print('Case #%d:' % (1))
    # print('SCC : ', scc)
    # print('SCC graph : ', sccG)
    # print('SCC parent : ', *p)   
    # print(*[findParent(i) for i in range(len(scc))])
    print(deg.count(0))