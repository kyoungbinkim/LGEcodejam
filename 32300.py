from sys import stdin

PRIME = 10**9 + 1

class Node:
    def __init__(self, num):
        self.n = num
        self.c= []
        self.cache = [[num], ]
        
    def add_child(self, child):            
        self.c.append(child)
    
    def get_childs(self, parent=None):
        return self.c

class Tree:
    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n+1)]
        for _ in range(n-1):
            u, v = map(int, stdin.readline().split())
            self.nodes[u].add_child(v)
            self.nodes[v].add_child(u)
        
        self.cache = [
            [[i]] for i in range( self.n+1 )
        ]
    
    def get_childs(self, num, gen=1):
        pass
    
        if len(self.cache[num]) > gen:
            return
    
    def calc(self, nxt):
        _nxt = [(1 << len(n)) -1 for n in nxt]
        # print(_nxt)
        ans = 1
        for _n in _nxt:
            ans *= _n 
            ans %= PRIME
        return ans
        
        
    def get_find(self, num):
        ans = 0
        cur = [self.nodes[num].get_childs()] # parent, [childs]
        print("num, cur : ", num, cur)
        if len(cur[0]) > 1:
            ans = 1
        else:
            return 0
        
        while True:
            nxt = []
            
            for group in cur:
                for _num in group:
                    if _num == num:
                        continue
                    nxt.append(self.nodes[_num].get_childs())
                    if len(nxt[-1]) == 1:
                        return ans
                    if len(cur) == 1:
                        nxt[-1] = nxt[-1].copy()
                        nxt[-1].remove(num)
                    
            
            print(num, nxt)
            
            ans += self.calc(nxt)
            cur = nxt


n = int(stdin.readline())
ans = 0
tr = Tree(n)

for i in range(1, n+1):
    ans += tr.get_find(i)
print(ans)



