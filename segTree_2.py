class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        # 리프 노드에 데이터를 저장합니다.
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # 내부 노드를 채웁니다.
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos, value):
        # 리프 노드를 업데이트합니다.
        pos += self.n
        self.tree[pos] = value
        # 내부 노드를 업데이트합니다.
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, left, right, value):
        return self._query(1, 0, self.n - 1, left, right, value)

    def _query(self, node, start, end, left, right, value):
        # 구간이 겹치지 않는 경우
        if start > right or end < left:
            return 0
        # 구간이 완전히 포함되는 경우
        if start >= left and end <= right:
            return 1 if self.tree[node] > value else 0
        # 구간이 부분적으로 겹치는 경우
        mid = (start + end) // 2
        left_count = self._query(2 * node, start, mid, left, right, value)
        right_count = self._query(2 * node + 1, mid + 1, end, left, right, value)
        return left_count + right_count

# 예제 배열
data = [1, 3, 5, 3, 9, 11, 3]

# 세그먼트 트리 생성
seg_tree = SegmentTree(data)

# 구간 내 특정 값보다 큰 원소의 개수 질의
print("구간 [1, 5] 내 값 4보다 큰 원소의 개수:", seg_tree.query(1, 5, 4))  # 구간 [1, 5] 내 값 4보다 큰 원소의 개수: 2

# 원소 업데이트
seg_tree.update(2, 7)

# 업데이트 후 구간 내 특정 값보다 큰 원소의 개수 질의
print("업데이트 후 구간 [1, 5] 내 값 4보다 큰 원소의 개수:", seg_tree.query(1, 5, 4))  # 구간 [1, 5] 내 값 4보다 큰 원소의 개수: 3
