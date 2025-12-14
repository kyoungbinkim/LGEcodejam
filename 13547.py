from sys import stdin

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        
        self.n = 2 ** (len(bin(self.n) )-2)
        
        self.tree = [set()] * (2 * self.n)
        self.build(data)
        
    def build(self, data):
        for i in range(len(data)):
            self.tree[self.n + i] = set([data[i]])
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i].union(self.tree[2 * i + 1])

    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        # 구간이 겹치지 않는 경우
        if start > right or end < left or node >= len(self.tree):
            return 0
        # 구간이 완전히 포함되는 경우
        if start >= left and end <= right:
            return len(self.tree[node])
            
        mid = (start + end) // 2
        left_count = self._query(2 * node, start, mid, left, right)
        right_count = self._query(2 * node + 1, mid + 1, end, left, right)
        return left_count + right_count
    
def sol():
    n = int(stdin.readline())
    leafs = list(map(int, stdin.readline().split()))
    seg_tree = SegmentTree(leafs)
    # ans = []
    for _ in range(int(stdin.readline())):
        cmd = list(map(int, stdin.readline().split()))
        print(seg_tree.query(cmd[0] - 1, cmd[1] - 1)) 
   
sol()
        
        
