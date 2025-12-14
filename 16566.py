from sys import stdin
from collections import deque

INF = 4_000_001

n,m,k = map(int, stdin.readline().split())

cards = list(map(int, stdin.readline().split()))
reds = list(map(int, stdin.readline().split()))
blues = []

cards.sort()

ans = []

class Node:
    def __init__(self, left, right, val=None):
        self.parent=None
        self.left = left
        self.right = right
        self.maxV = max(left.maxV, right.maxV)  if val is None else val
        self.minV = min(left.minV, right.minV)  if val is None else val
        
    def delete(self):
        if self.parent == None:
            return
        if self.parent.left == self:
            self.parent.left = None
        else:
            self.parent.right = None
        
        self.parent.updateVal()
        
    def updateParent(self, parent):
        self.parent = parent
    
    def isLeaf(self):
        return self.minV == self.maxV
    
    def updateVal(self):
        if self.left is None and self.right == None:
            self.maxV = -INF
            self.minV = INF
            self.delete()
        elif self.right and self.left:
            self.maxV = max(self.left.maxV, self.right.maxV)  
            self.minV = min(self.left.minV, self.right.minV)  
        elif self.right:
            self.maxV  = self.right.maxV
            self.minV  = self.right.minV
        elif self.left:
            self.maxV  = self.left.maxV
            self.minV  = self.left.minV
        
        if self.parent:
            self.parent.updateVal()
        
        
    def findVal(self, val):
        # print(f"findVal : {self.minV}, {self.maxV}")
        if self.isLeaf():
            return self
        
        if self.left == None:
            return self.right.findVal(val)
        elif self.right == None:
            return self.left.findVal(val)

        
        if self.left.maxV <= val:
            _f = self.right.findVal(val)
        else:
            _f = self.left.findVal(val)
        return _f
    
leafs = deque([Node(None, None, v) for v in cards])

while len(leafs)>1:
    l, r = leafs.popleft(), leafs.popleft()
    
    if l.maxV > r.minV:
        leafs.append(l)
        l = r
        r = leafs.popleft()

    newNode = Node(l, r)
    l.updateParent(newNode)
    r.updateParent(newNode)
    leafs.append(newNode)

rt = leafs[0]

for r in reds:
    _node =  rt.findVal(r)
    print(_node.minV)
    _node.delete()
    del _node