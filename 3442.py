from sys import stdin

rl = stdin.readline

def ccw(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    cp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if cp > 0:
        return 1  # 반시계 방향
    elif cp < 0:
        return -1  # 시계 방향
    else:
        return 0  # 일직선

def sol():
    n = int(stdin.readline())
    if n==0:
        return False
    
    points = [list(map(int, rl().split())) for _ in range(n)]
    
    return True
    
    
while sol():
    rl()
    pass
    
    
    
