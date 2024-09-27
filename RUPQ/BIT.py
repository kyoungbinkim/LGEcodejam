'''
Binary Indexed Tree for Point Query and Range Update

O(q * log n) + O(n * log n)
q : 쿼리의 개수
n : 데이터의 개수

https://nahwasa.com/entry/%ED%8E%9C%EC%9C%85-%ED%8A%B8%EB%A6%ACFenwick-tree-BIT-%EA%B8%B0%EB%B3%B8-2D-lazy-propagationrange-update-point-query-range-update-range-query#range_update_+_point_query
'''

class BIT:
    def __init__(self, n, leafs):
        self.n = n
        self.leafs = leafs
        self.tree = [0 for _ in range(n+1)]
 
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
    
    def getPoint(self, idx):
        return self.__getSum(idx) + self.leafs[idx]


def test():
    bit = BIT(12, [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3, 3])
    
    print("getPoint(5) : ", bit.getPoint(5))
    print("getPoint(3) : ", bit.getPoint(3))
    

test()
