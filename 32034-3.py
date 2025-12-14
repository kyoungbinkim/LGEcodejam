from sys import stdin
from collections import deque

def updateDeque(q):
    while q and q[0][0] == 'H':
        q.popleft()
    
    cur = ['H', 0]
    while q and q[-1][0] == 'H':
        cur[1] += q.pop()[1]
    if cur[1]:
        q.append(cur)
    return q

def updateStatus(q):
    q = updateDeque(q)
    ans = 0
    if len(q) > 1 and q[-1][0] == 'H' and q[-1][1] >= 2 :
        ans += len(q)
        tmp = q.pop()
        if tmp[1] == 3:
            q.append(['H',1])
    if len(q) and q[-1][0] == 'T' and q[-1][1] == 2:
        ans += 1
        q.pop()
        q.append(['H',2])
        ans += updateStatus(q)

    return ans
            
def sol():
    n = int(stdin.readline())
    coins = stdin.readline().rstrip()
    
    coinsList, ans = deque(), 0
    for c in coins:
        if len(coinsList) == 0:
            if c == 'T':
                coinsList.append([c,1])
            continue
        
        coinsList = updateDeque(coinsList)
        
        if coinsList[-1][0] == c:
            coinsList[-1][1] += 1
        else:
            coinsList.append([c,1])
        
        ans += updateStatus(coinsList)
        # print(coinsList, ans)
    coinsList = updateDeque(coinsList)
    if len(coinsList):
        print(-1)
    else:
        print(ans)

for _ in range(int(stdin.readline())):
    sol()