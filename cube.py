from sys import stdin

u, d ,r ,l = (-1,0), (1,0), (0,1), (0,-1)
dirs = [u,d,r,l]

class Cube:
    def __init__(self):
        self.b = [
            list(map(int, stdin.readline().split())) for _ in range(6)
        ]
        self.pos = [None for _ in range(7)]
        for i in range(6):
            for j in range(6):
                if self.b[i][j] != 0:
                    self.pos[self.b[i][j]] = (i,j)
        
        self.canMake()

    def canMake(self):
        ones = 0
        for i in range(1,7):
            flag, find1, find2 = False, -1, -1
            for d in dirs:
                # print(i,d)
                find1 = self.__goStraight(self.pos[i], d)
                find2 = self.__goZigzag(self.pos[i], d)
                # print()
                
                ones = find1 if i== 1 and find1 > 0 else ones
                ones = find2 if i== 1 and find2 > 0 else ones
                
                if find1 > 0 or find2 > 0:
                    if flag or (find1 > 0 and find2 > 0):
                        flag = False
                        break
                    flag = True
        
            if not flag:
                print(0)
                return
        print(ones)
    
    def __goStraight(self, p, d):
        x,y = p
        
        for _ in range(2):
            x += d[0]
            y += d[1]
            
            if (x,y) in self.pos:
                continue
            return -1
        return self.pos.index((x,y))

    def __goZigzag(self, p, d):
        x,y = p
        x += d[0]
        y += d[1]
        # print((x,y),d)
        if (x,y) not in self.pos:
            return -1
        
        for it in range(2):
            for l in range(1,4):
                mx = x +  d[1] * ((-1)**it * l)
                my = y +  d[0] * ((-1)**it * l)
                # print((mx,my), self.pos)
                if (mx,my) in self.pos:
                    mx += d[0]
                    my += d[1]
                    if (mx,my) in self.pos:
                        return self.pos.index((mx,my))
        
        return -1

Cube()


'''
0 0 0 0 0 0
0 3 0 0 0 0
0 2 4 0 0 0
0 1 6 5 0 0
0 0 0 0 0 0
0 0 0 0 0 0

0 0 0 0 0 0
0 3 5 0 0 0
1 2 4 6 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

0 0 0 0 0 0
0 3 0 0 0 0
1 2 4 6 0 0
0 0 0 5 0 0
0 0 0 0 0 0
0 0 0 0 0 0


0 0 0 0 0 0
1 3 0 0 0 0
0 2 4 0 0 0
0 0 6 5 0 0
0 0 0 0 0 0
0 0 0 0 0 0

0 0 0 0 0 0
0 0 3 0 0 0
0 2 4 6 0 0
0 1 0 5 0 0
0 0 0 0 0 0
0 0 0 0 0 0

'''