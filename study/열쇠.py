from sys import stdin
from collections import deque

cmap = {
    '*' : 1,
    '.' : 0
}

dir = [
    (0,1),(0,-1),(1,0),(-1,0)
]

class KEYCLASS:
    def __init__(self):
        self.ans = 0
        self.keys = set()
        self.keyMap = {}
        self.visit = set()
        self.board = []
        self.que = deque()
        self.n, self.m = map(int, stdin.readline().split())
        for i in range(self.n):
            tmp = []
            for (j,c) in enumerate(stdin.readline().strip()):
                if c == '.' or c == '*':
                    tmp.append(cmap[c])
                elif c == '$':
                    self.pos = (i,j)
                    tmp.append('$')
                else:
                    tmp.append(c)
                    if c.isupper():
                        if self.keyMap.get(c) == None:
                            self.keyMap[c] = []
                        self.keyMap[c].append((i,j))
                
                if  c != '*' and  (i==0 or i == self.n-1 or j==0 or j==self.m-1) :
                    self.visit.add((i,j))
                    if c =='.' or c == '$':
                        self.que.append((i,j))
                        self.ans+= c=='$'
                    elif c.islower():
                        self.keys.add(c)
                        self.que.append((i,j))

            self.board.append(tmp)

        # for l in self.board:
        #     print(l)
        
        
        for c in stdin.readline().strip():
            self.keys.add(c)

        for (x, y) in self.visit:
            if type(self.board[x][y]) == type('') and  self.board[x][y].isupper():
                if self.board[x][y].lower() in self.keys:
                    self.que.append((x,y))

        # print(self.keys)
        # print(self.keyMap)
        # print(self.visit, self.que)
    
    def bfs(self):
        
        while len(self.que):
            x, y = self.que.popleft()
            for dx, dy in dir:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= self.n or ny < 0 or ny >= self.m:
                    continue
                if (nx,ny) in self.visit:
                    continue
                if self.board[nx][ny] == 1:
                    continue
                if self.board[nx][ny] == 0:
                    self.visit.add((nx,ny))
                    self.que.append((nx,ny))
                    continue

                if self.board[nx][ny] == '$':
                    self.visit.add((nx,ny))
                    self.que.append((nx,ny))
                    self.ans+= 1
                    continue
                
                if self.board[nx][ny].islower():
                    self.keys.add(self.board[nx][ny])
                    self.que.append((nx,ny))
                    self.visit.add((nx,ny))

                    for (xx, yy) in self.keyMap[self.board[nx][ny].upper()]:
                        # print(self.board[nx][ny], (xx,yy), (xx,yy) in self.visit)
                        if (xx,yy) in self.visit:
                            self.que.append((xx,yy))

                elif self.board[nx][ny].isupper():
                    self.visit.add((nx,ny)) 
                    if self.board[nx][ny].lower() in self.keys:
                        self.que.append((nx,ny))

        print(self.ans)

t = int(stdin.readline())
for _ in range(t):
    kc = KEYCLASS()
    kc.bfs()


