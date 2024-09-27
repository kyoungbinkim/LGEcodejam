

class BIT:
    def __init__(self, n, leafs):
        self.n = n
        self.bit1 = [0 for _ in range(n+1)]
        self.bit2 = [0 for _ in range(n+1)]
        self.acc = [leafs[0]]
        for i in range(1, n):
            self.acc.append(self.acc[-1] + leafs[i])
        
        
    def __getSum(self, tree, idx) :
        s = 0  
        idx = idx + 1
        while idx > 0:

            s += tree[idx]
            idx -= idx & (-idx)
        return s
    
    def __updateBit(self, tree, idx, val):
        idx = idx + 1
        while idx <= self.n:
            tree[idx] += val
            idx += idx & (-idx)
    
    # return sum of arr[0..idx]
    def __summation(self, idx) -> int:
        return (self.__getSum(self.bit1, idx) * idx) - self.__getSum(self.bit2, idx)
 
    def updateRange(self, val, l, h) -> None:
    
        self.__updateBit(self.bit1, l, val)
        self.__updateBit(self.bit2, h + 1, -val)
    
        self.__updateBit(self.bit2, l, val * (l - 1))
        self.__updateBit(self.bit2, h + 1, -val * h)
        
    # sum of arr[l..h]
    def rangeSum(self, l, h) -> int:
        return self.__summation(h) - self.__summation(l-1) + self.acc[h] - self.acc[l-1]


def test():
    bit = BIT(12, [1,2,3,4,5,6,1,2,3,4,5,6])
    print("rangeSum(1, 5) : ", bit.rangeSum(1, 5))
    print("rangeSum(3, 9) : ", bit.rangeSum(3, 9))
    
    bit.updateRange(3, 1, 5)
    print("rangeSum(1, 5) : ", bit.rangeSum(1, 5))
test()