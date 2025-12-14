from sys import stdin


dirs = [(1,1), (0,2), (-1, 1), (-1, -1), (0, -2), (1,-1)]
cnt = [0 for _ in range(6)]
cnt[0] = float('inf')
for i in range(1,5):
    cnt[i] = 1
ans = [0,1,2,3,4]

corMap = {
    (0,-1) : 1,
    (1,0) :2,
    (0,1) : 3,
    (-1, 0): 4
}

cur = (-1,0)
dirSelector = 0

def nxtDir(pos, ds):
    for i in range(1,6):
        nxt= (pos[0] + dirs[(ds+i) %6][0] , pos[1] + dirs[(ds+i) %6][1])
        if corMap.get(nxt) != None:
            return (ds+i-1) % 6 , (pos[0] + dirs[(ds+i-1) %6][0] , pos[1] + dirs[(ds+i-1) %6][1])

def findNext(nxt):
    exceptinon = []
    for dx,dy in dirs:
        mx,my= nxt[0] + dx, nxt[1] + dy
        if corMap.get((mx,my)) != None:
            exceptinon.append(corMap[(mx,my)])
    tmp = [0, float('inf')]
    for i in range(1,6):
        if i in exceptinon:
            continue
        if cnt[i] < tmp[1]:
            tmp = [i, cnt[i]]
    
    return tmp[0]
        
for _ in range(10000):
    dirSelector, nxt = nxtDir(cur, dirSelector)
    idx = findNext(nxt)
    
    corMap[nxt] = idx
    cur = nxt
    cnt[idx] += 1
    ans.append(idx)
    

cor = []
for _ in range(int(stdin.readline())):
    cor.append(ans[int(stdin.readline())])

for c in cor:
    print(c)