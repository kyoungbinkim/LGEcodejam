from sys import stdin

rl = stdin.readline

dir = [
    (-1,0), (1,0), (0,1), (0,-1)
]

class FisherClass:
    def __init__(self):
        self.ans = 0
        self.r, self.c, self.m = map(int, rl().split())
        
        self.sharks = []
        for _ in range(self.m):
            r, c, s, d, z = map(int,rl().split())
            self.sharks.append(
                [r-1, c-1, s, d-1, z]
            )
        
    def deleteShark(self):
        y,idx = float('inf'), None
        for i in range(len(self.sharks)):
            if i == self.sharks[i][1] and self.sharks[i][0] < y:
                y = self.sharks[i][0]
                idx = i
        
        if idx:
            self.ans += self.sharks[-1]
            self.sharks.pop(idx)
    
    def moveShark(self):
        pass