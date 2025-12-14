from sys import stdin
from collections import deque
rl = stdin.readline

def updateQueue(q):
    cur = ['H', 0]
    
    while q and q[-1][0] == 'H':
        cur[1] += q.pop()[1]
    if cur[1]:
        q.append(cur)
    return q

def sol():
    n = int(rl())
    coins = rl().rstrip()
    
    stck, ans = deque(), 0
    
    for i,c in enumerate(coins):
        stck = updateQueue(stck)
        if len(stck) == 0:
            stck.append([c,1])
            continue
        
        if c == 'H':
            if stck[-1][0] == 'H':
                stck[-1][1] += 1
                continue
            stck.append(['H',1])
        elif c == 'T':
            if stck[-1][0] == 'T':
                tmp = stck.pop()
                ans += (tmp[1] + 1) // 2
                stck.append(['H', tmp[1] + 1])
            else:
                if len(stck) > 1 and stck[-2][0] == 'T' and stck[-1][0] =='H' and stck[-1][1] % 2 == 0:
                    ans += stck[-1][1] + (stck[-2][1] + 1) // 2
                    stck[-2][0] = 'H'
                    stck.append(['H',1])
                    continue
                stck.append(['T',1])
    stck = updateQueue(stck)
    if len(stck) > 1:
        print(-1)
    else:
        print(ans)
            

for _ in range(int(stdin.readline())):
    sol()