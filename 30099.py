from sys import stdin


n = int(stdin.readline())
CHECK = [
    (-1,-1), (-1,0),(0,-1), (0,1), (-1, 1)
]

def cnt_zero(pos, b):
    x,y = pos
    
    cnt = 0
    for dx, dy in CHECK:
        mx, my = x+dx, y+dy
        
        if my < 0  or my >= n or mx < 0 or mx>= n:
            continue
        
        cnt += 1 - b[mx][my]
        print(pos, cnt)
    return cnt

def make_zero_cnt_list(ans, hints):
    y = len(ans)-1
    ret = []
    for i in range(n):
        print(hints[y][i])
        ret.append(hints[y][i] - cnt_zero((y, i), ans))
    return ret

ans = [list(map(int, stdin.readline().split()))]
hints = [list(map(int, stdin.readline().split())) for _ in range(n)]

print(ans, hints)

for idx in range(n-1):
    tmp = [-1 for _ in range(n)]
    zeros = make_zero_cnt_list(ans,hints)
    
    tmp[2] = 0 if zeros[1] > zeros[0] else 1
    tmp[-3] = 0 if zeros[-2] >  zeros[-1] else 1
    
    
    for j in range(1, n-1):
        if zeros[j] == 0:
            for d in range(-1, 2):
                tmp[j+d] = 1
        elif zeros[j] == 3:
            for d in range(-1, 2):
                tmp[j+d] = 0
        else:
            if j < n-1:
                if zeros[j+1] - zeros[j]  == 1:
                    if j+2 <= n-1:
                        tmp[j+1] = 0
                    if j-1 >= 0:
                        tmp[j-1] = 1
                elif zeros[j+1] - zeros[j]  == -1:
                    if j+2 <= n-1:
                        tmp[j+1] = 1
                    if j-1 >= 0:
                        tmp[j-1] = 0
                        
    for j in range(n):
        z = 0
        for k in range(-1, 2):
            if j + k >= 0 and j+k < n:
                z += tmp[j+k] == 0
    
    print(f"idx: {idx}\nzeros:{zeros}\ntmp:{tmp}\n")
    
    break