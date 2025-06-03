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



'''
2 번째 방법
'''

from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        stack.append(v)

    def reverseGraph(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def getScc(self):
        stack = []
        visited = [False] * (self.V)
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        gr = self.reverseGraph()

        visited = [False] * (self.V)
        sccs = []
        while stack:
            i = stack.pop()
            if not visited[i]:
                scc = []
                gr.dfsUtil(i, visited, scc)
                sccs.append(scc)
        return sccs

    def dfsUtil(self, v, visited, scc):
        visited[v] = True
        scc.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfsUtil(i, visited, scc)