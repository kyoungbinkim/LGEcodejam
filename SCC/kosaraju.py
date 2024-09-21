'''
'''


def kosaraju(_n, _G, _revG):
    
    n = _n # 노드의 개수
    G = _G # 정방향
    revG = _revG # 역방향
    visit = set()
    order = [] # 먼저 방문마친 노드를 저장
    scc = [] # scc를 저장
    
    def dfs(idx):
        visit.add(idx)
        for i in G[idx]:
            if i not in visit:
                visit.add(i)
                dfs(i)
        order.append(idx)
        
    def revDfs(idx, e):
        e.append(idx)
        for i in revG[idx]:
            if i not in visit:
                visit.add(i)
                revDfs(i, e)
    
    for i in range(n):
        if i not in visit:
            visit.add(i)
            dfs(i)
    
    visit = set()
    
    while len(order):
        i = order.pop()
        if i not in visit:
            e = []
            visit.add(i)
            revDfs(i, e)
            scc.append(e)
    
    return scc


v,e = map(int, input().split())
g = [[] for _ in range(v+1)]
revg = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int, input().split())
    g[a].append(b)
    revg[b].append(a)

scc = kosaraju(v, g, revg)
print(scc)
            