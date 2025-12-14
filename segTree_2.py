class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        # 리프 노드에 데이터를 저장
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # 내부 노드를 채움
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, pos, value):
        # 리프 노드 업데이트
        pos += self.n
        self.tree[pos] = value
        # 내부 노드 업데이트
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]

    def query(self, left, right):
        # 구간 합을 구하는 재귀 함수
        def query_recursive(left, right, pos, l, r):
            if left > right:
                return 0
            if left == l and right == r:
                return self.tree[pos]
            mid = (l + r) // 2
            return query_recursive(left, min(right, mid), pos * 2, l, mid) + \
                   query_recursive(max(left, mid + 1), right, pos * 2 + 1, mid + 1, r)

        return query_recursive(left, right, 1, 0, self.n - 1)

# 예제 사용
data = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(data)

# 구간 합 쿼리
print(seg_tree.query(1, 3))  # 구간 [1, 3]의 합: 3 + 5 + 7 = 15

# 업데이트
seg_tree.update(2, 10)  # 인덱스 2의 값을 10으로 업데이트
print(seg_tree.query(1, 3))  # 구간 [1, 3]의 합: 3 + 10 + 7 = 20
