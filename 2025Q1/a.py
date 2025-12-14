from sys import stdin

DIR = {
    'u' : [-1,0],
    'd' : [1,0],
    'l' : [0,-1],
    'r' : [0,1]
}

O = {
    1: [DIR['l'], DIR['u']],
    2: [DIR['u'], DIR['r']],
    3: [DIR['l'], DIR['d']],
    4: [DIR['d'], DIR['r']]
}

def filld(_f):
    return _f | (1<<0)

def fillr(_f):
    return _f | (1<<1)

def fillu(_f):
    return _f | (1<<2)

def filll(_f):
    return _f | (1<<3)

def fillBox():
    return 15

class Rec:
    def __init__(self):
        self.dir, self.d, self.x, self.y = map(int, stdin.readline().split())
        # y = m(x - xn) + yn
        _dir = O[self.dir]
        self.dx, self.dy = _dir[0][1] + _dir[1][1], _dir[0][0] +  _dir[1][0]
        self.m = self.dx * self.dy
        self.xn = self.x + self.dx * self.d
        self.yn = self.y
        
        self.ran = [
            min(self.x , self.x + self.dx*self.d),
            max(self.x , self.x + self.dx*self.d)
        ]
        
        # print(f"""
        #       self.dir : {self.dir}
        #       _dir : {_dir}
        #       self.d : {self.d}
        #       self.m : {self.m}
        #       (x,y) : ({self.x}, {self.y})
        #       self.xn : {self.xn}
        #       self.yn : {self.yn}
        #       """)
                
    def isIn(self, _x, _y):
        if _x < self.ran[0] or _x > self.ran[1]:
            return False
        
        th_pos = self.m * (_x - self.xn) + self.yn
        _ran = [
            min(self.y,  th_pos), max(self.y, th_pos)
        ]
        
        if _ran[0] <= _y <= _ran[1]:
            return True
        return False
    
    def calcPos(self, _x):
        return self.m * (_x - self.xn) + self.yn
    
def sol():
    n = int(stdin.readline())
    
    rec = [Rec() for _ in range(n)]
    pos = [[set() for _ in range(101)] for _ in range(101)]
    board = [[0 for _ in range(101)] for _ in range(101)]
    
    for x in range(101):
        for y in range(101):
            for k,r in enumerate(rec):
                if r.isIn(x,y):
                    pos[y][x].add(k)
    
    ans = 0
    for x in range(101):
        for y in range(101):
            for k in pos[y][x]:
                if x and y  and  board[y-1][x-1] & (1<<2 | 1<<1) !=  (1<<2 | 1<<1) :
                    if k in pos[y-1][x] and k in pos[y][x-1]:
                        board[y-1][x-1] |= (1<<2 | 1<<1)
                if x == 100 or y==100:
                    continue
                
                if board[y][x] == 15:
                    continue
                
                a,b,c = k in pos[y][x+1], k in pos[y+1][x], k in pos[y+1][x+1]
                if a and b and c :
                    board[y][x] = fillBox()
                    continue
                
                if a and b:
                    board[y][x] |= (1<<0 | 1<<3)
                elif a and c:
                    board[y][x] |= (1<<0 | 1<<1)
                elif b and c:
                    board[y][x] |= (1<<2 | 1<<3)
                
    
    for i in range(100):
        for j in range(100):
            
            if board[i][j]:
                ans += 0.25 * bin(board[i][j]).count('1')
                # print(f"({j}, {i}) -> {ans}")
    print("{:.2f}".format(ans))
            
    
for _ in range(int(stdin.readline())):
    sol()