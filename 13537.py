from sys import stdin

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [[0,0,0]] * (2 * self.n)
        self.build(data)

    def build(self, data):
        # 리프 노드에 데이터를 저장합니다.
        for i in range(self.n):
            self.tree[self.n + i] = [data[i], data[i], 1]
        # 내부 노드를 채웁니다.
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = [
                min(self.tree[2 * i][0], self.tree[2 * i + 1][0]),
                max(self.tree[2 * i][1], self.tree[2 * i + 1][1]),
                self.tree[2 * i][2] + self.tree[2 * i + 1][2]
            ]

    def update(self, pos, value):
        # 리프 노드를 업데이트합니다.
        pos += self.n
        self.tree[pos] = value
        # 내부 노드를 업데이트합니다.
        while pos > 1:
            pos //= 2
            self.tree[pos][0] = min(self.tree[2 * pos][0], self.tree[2 * pos + 1][0])
            self.tree[pos][1] = max(self.tree[2 * pos][1], self.tree[2 * pos + 1][1])

    def query(self, left, right, value):
        return self._query(1, 0, self.n - 1, left, right, value)

    def _query(self, node, start, end, left, right, value):
        # 구간이 겹치지 않는 경우
        if start > right or end < left or node >= len(self.tree):
            return 0
        # 구간이 완전히 포함되는 경우
        if start >= left and end <= right:
            if self.tree[node][0] > value:
                return self.tree[node][2]
            elif self.tree[node][1] <= value:
                return 0
            
        mid = (start + end) // 2
        left_count = self._query(2 * node, start, mid, left, right, value)
        right_count = self._query(2 * node + 1, mid + 1, end, left, right, value)
        return left_count + right_count
    
def sol():
    n = int(stdin.readline())
    leafs = list(map(int, stdin.readline().split()))
    seg_tree = SegmentTree(leafs)
    # ans = []
    for _ in range(int(stdin.readline())):
        cmd = list(map(int, stdin.readline().split()))
        print(seg_tree.query(cmd[0]-1, cmd[1]-1, cmd[2]))
   
sol()
        