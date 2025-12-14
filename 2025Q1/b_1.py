from sys import stdin
from heapq import heappop, heappush
from collections import deque

def calcScore(_h,day):
    return _h[2] - (day- _h[1]) * _h[3]

k,n = map(int, stdin.readline().split())

# s, e, p, d
items, h = [
    tuple(map(int, stdin.readline().split())) for _ in range(k)
],[]

items.sort()
items = deque(items)

endTime = 0 

tmpDay, tmpScore = None, None
ansScore = float('inf')

d_sum = 0
score = 0
while items:
    if h:
        endDay = h[0][0]
        while h and endDay == h[0][0]:
            e,s,p,d = heappop(h)
            d_sum -= d
            score -= calcScore([ e,s,p,d], endDay)
    
    if len(h) == 0:
        itm = items.popleft()
        heappush(h, (itm[1], itm[0], itm[2], itm[3]))
        d_sum += itm[3]
        
    
    while items and items[0][0] <= h[0][0]:
        itm = items.popleft() 
        heappush(h, (itm[1], itm[0], itm[2], itm[3]))
        d_sum += itm[3]
    
    
    score = sum([ calcScore(tmp, h[0][0]) for tmp in h])
    print(h, score)

while len(h) >=n:
    endDay = h[0][0]
    while h and endDay == h[0][0]:
        heappop(h)
    
    if len(h) < n:
        break
        
    score = sum([ calcScore(tmp, h[0][0]) for tmp in h])
    print(h, score)
    