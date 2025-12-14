from sys import stdin

rl = stdin.readline

n = int(rl())

door = tuple(map(int, rl().split()))

points = []
areas = []

def calcArea(p1, p2, p3):
    x1,y1 = p1
    x2,y2 = p2
    x3, y3 = p3
    
    return abs(x1 * y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2- x1*y3) / 2
    
for _ in range(n-1):
    points.append(tuple(map(int, rl().split())))
    
    if len(points) >= 2:
        areas.append(calcArea(door, points[-2], points[-1]))

halfArea = sum(areas) / 2
accArea = 0
for i in range(1, n-1):
    accArea += areas[i-1]
    
    if accArea == halfArea:
        ans = points[i]
        break
    elif accArea > halfArea:
        diffArea = accArea - halfArea
        
        m, n = halfArea-(accArea-areas[i-1]),accArea - halfArea
                
        x1,y1 = points[i-1]
        x2,y2 = points[i]

        ans = ((m*x2 + n*x1) / (m+n), (m*y2 + n*y1) / (m+n))
        
        break

print(*ans)