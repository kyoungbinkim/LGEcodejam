from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**7)

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

n,m = map(int, stdin.readline().split())

sccG = Graph(n)

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    sccG.addEdge(a-1,b-1)

scc= sccG.getScc()
print('Yes' if len(scc) == 1 else 'No')