'''
Binary Indexed Tree

O(q * log n) + O(n * log n)
q : 쿼리의 개수
n : 데이터의 개수

'''

class BIT:
    def __init__(self, n, leafs):
        self.n = n
        self.tree = [0 for _ in range(n+1)]
        for idx in range(n):
            self.__updeteTree(idx, leafs[idx])
 
    
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
        return self.__getSum(idx) - self.__getSum(idx-1)


def test():
    bit = BIT(12, [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3, 3])
    
    print("getPoint(5) : ", bit.getPoint(5))
    print("getPoint(3) : ", bit.getPoint(3))
    
    print("getRange(2, 5) : ", bit.getRange(2, 5))
    print("getRange(3, 6) : ", bit.getRange(3, 6))

test()
