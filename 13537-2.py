from sys import stdin
from bisect import bisect_left, bisect_right

# print(bisect_left([1,2,3,4,4,5], 3))
# print(bisect_right([1,2,3,4,4,5], 0))


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        
        self.n = 2 ** (len(bin(self.n) )- 2)
        
        self.tree = [[]] * (2 * self.n)
        self.build(data)

    def __merge(self, a, b):
        tmp = []
        i,j = 0, 0
        
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                tmp.append(a[i])
                i += 1
            else:
                tmp.append(b[j])
                j += 1
        
        while i < len(a):
            tmp.append(a[i])
            i += 1
        while j < len(b):
            tmp.append(b[j])
            j += 1
        return tmp
        
    def build(self, data):
        # 리프 노드에 데이터를 저장합니다.
        for i in range(len(data)):
            self.tree[self.n + i] = [data[i]]
        # 내부 노드를 채웁니다.
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.__merge(self.tree[2 * i], self.tree[2 * i + 1])
        # print(self.tree)

    def query(self, left, right, value):
        return self._query(1, 0, self.n - 1, left, right, value)

    def _query(self, node, start, end, left, right, value):
        # 구간이 겹치지 않는 경우
        if start > right or end < left or node >= len(self.tree):
            return 0
        # 구간이 완전히 포함되는 경우
        if start >= left and end <= right:
            idx = bisect_right(self.tree[node], value)
            return len(self.tree[node]) - idx
            
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
        
        
