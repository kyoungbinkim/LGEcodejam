
p = [i for i in range(10)]

def findParent(x):
    if p[x] != x:
        p[x] = findParent(p[x])
    return p[x]

def union(a, b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
        

# UnionFind
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n # rank 그 노드가 루트인 트리의 높이

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        rtX = self.find(x)
        rtY = self.find(y)
        if rtX != rtY:
            if self.r[rtX] > self.r[rtY]:
                self.p[rtY] = rtX
            elif self.r[rtX] < self.r[rtY]:
                self.p[rtX] = rtY
            else:
                self.p[rtY] = rtX
                self.r[rtX] += 1