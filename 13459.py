from sys import stdin
from collections import deque

u,d,l,r =(-1,0), (1,0), (0,-1), (0,1)
DIRS = [u,d,l,r]

n,m = map(int, stdin.readline().split())
b,pos,dest = [], [None, None], None # R, B  빨간공을 빼내야함
for i in range(n):
    l = stdin.readline().strip()
    line = []
    
    for j in range(m):
        if l[j] == '#':
            line.append(-1)
            continue
        elif l[j] == 'R':
            pos[0] = (i,j)
        elif l[j] == 'B':
            pos[1] = (i,j)
        elif l[j] == 'O':
            dest = (i,j)
            pass
            
        line.append(0)
    b.append(line)

def updatePos(pos, d):
    dx, dy = d
    new, flag = [None, None], False
    
    new[0] = (pos[0][0] + dx, pos[0][1] + dy)
    new[1] = (pos[1][0] + dx, pos[1][1] + dy)
    
    if pos[0][0] and b[new[0][0]][new[0][1]] == -1 or new[0] == pos[1]:
        new[0] = pos[0]
    else:
        flag = True
    
    if pos[1][0] and b[new[1][0]][new[1][1]] == -1 or new[1] == pos[0]:
        new[1] = pos[1]
    else:
        flag = True
    
    return new, flag    

def DFS(pos, dirs):
    if len(dirs) > 10:
        return
    findRed, findBlue = False, False
    while True:
        new, flag = updatePos(pos, dirs[-1])
        if new[1] == dest:
            findBlue = True 
        elif new[0] == dest:
            findRed = True

        if not flag:
            break
        else:
            pos = new
            if findRed:
                pos[0] = (-1,-1)
            if findBlue:
                pos[1] = (-1,-1)
    if findBlue:
        return
    if findRed:
        print(1)
        exit()
        
    for d in DIRS:
        if d == dirs[-1]:
            continue
        DFS(pos, dirs + [d])
        
        
for d in DIRS:
    DFS(pos, [d])
print(0)



'''
3 5
#####
#ORB#
#####
'''

'''
10 10
##########
#.R......#
##.......#
#O.......#
#........#
#........#
#........#
#........#
#B.......#
##########
'''