'''
신장 트리(Spanning Tree)
신장 트리는 그래프의 모든 정점을 포함하면서 사이클이 없는 부분 그래프입니다. 
즉, 신장 트리는 그래프의 모든 정점을 연결하면서 간선의 수가 최소인 트리입니다. 신장 트리의 특징은 다음과 같습니다:

 - 모든 정점을 포함: 신장 트리는 원래 그래프의 모든 정점을 포함합니다.
 - 사이클이 없음: 신장 트리는 사이클을 포함하지 않습니다.
 

최소 신장 트리(Minimum Spanning Tree, MST)
 - 최소 가중치 합: 최소 신장 트리는 간선의 가중치 합이 최소입니다.

'''

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


# 엣지의 길이가 작은 순서로 정렬해서 같은 루트에 속해있지 않은 노드들을 연결한다.
def kruskal(edges, num_vertices):
    # 간선을 가중치에 따라 정렬
    edges.sort(key=lambda x: x[2])

    # Union-Find 구조 초기화
    uf = UnionFind(num_vertices)
    mst = []

    for edge in edges:
        u, v, weight = edge
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append(edge)

    return mst


def test():

    # 예제 그래프
    edges = [
        (0, 1, 4),
        (0, 7, 8),
        (1, 2, 8),
        (1, 7, 11),
        (2, 3, 7),
        (2, 5, 4),
        (2, 8, 2),
        (3, 4, 9),
        (3, 5, 14),
        (4, 5, 10),
        (5, 6, 2),
        (6, 7, 1),
        (6, 8, 6),
        (7, 8, 7)
    ]

    num_vertices = 9

    mst = kruskal(edges, num_vertices)
    print("최소 신장 트리의 간선:")
    for edge in mst:
        print(edge)
