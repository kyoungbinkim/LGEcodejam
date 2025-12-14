from sys import stdin

class BIT:
    def __init__(self, n, leafs):
        self.n = n
        self.leafs = leafs
        self.tree = [0 for _ in range(n+1)]
        # for idx in range(n):
        #     self.__updeteTree(idx, leafs[idx])
 
    
    def __updeteTree(self,idx, value):
        idx = idx + 1
        while (idx <= self.n):
            self.tree[idx] += value
            idx += idx & (-idx)

    # retunr sum of leafs[0..idx]
    def __getSum(self, idx):
        sum = 0
        idx = idx + 1
        while (idx > 0):
            sum += self.tree[idx]
            idx -= idx & (-idx)
        return sum
    
    def update(self, l, h, val):
        self.__updeteTree(l, val)
        self.__updeteTree(h+1, -val)
    
    def getRange(self, l, h):
        return self.__getSum(h) - self.__getSum(l-1)
    
    def getPoint(self, idx):
        return self.__getSum(idx) + self.leafs[idx]


n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
qNum = int(stdin.readline())

bit = BIT(n, a)

for _ in range(qNum):
    q = list(map(int, stdin.readline().split()))
    if q[0] == 1:
       bit.update(q[1]-1, q[2]-1, q[3])
    else:
        print(bit.getPoint(q[1]-1))
    
    
    