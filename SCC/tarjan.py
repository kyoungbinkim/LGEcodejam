'''
ref : https://storyofvector7.tistory.com/44 
complexity : O(V+E)
'''

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

v,e = map(int, input().split())
g = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int, input().split())
    g[a].append(b)
        
print(tarjan(v, g))