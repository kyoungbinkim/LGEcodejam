from sys import stdin
from bisect import bisect_left, bisect_right

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
        for i in range(len(data)):
            self.tree[self.n + i] = [data[i]]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.__merge(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left, right, value):
        # print("query : ", left, right, value)
        return self._query(1, 0, self.n - 1, left, right, value)

    def _query(self, node, start, end, left, right, value):
        if start > right or end < left or node >= len(self.tree):
            return 0
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
    ans = 0
    for _ in range(int(stdin.readline())):
        cmd = list(map(int, stdin.readline().split()))
        ans = seg_tree.query((cmd[0] ^ ans) - 1,( cmd[1] ^ ans) - 1, cmd[2] ^ ans)
        print(ans)
sol()
        
        
