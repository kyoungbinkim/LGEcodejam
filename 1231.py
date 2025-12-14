from sys import stdin
from heapq import heappop, heappush

c,d,m = map(int, stdin.readline().split())

stocks = [list(map(int, stdin.readline().split())) for _ in range(c)]

def dpRoutine(_m, days, stck):
    
    


for i in  range(d-1):
    h = []
    for j in range(c):
        roi = stocks[j][i+1] /  stocks[j][i] 
        if roi < 1 :
            continue
        
        heappush(h, [-roi, j])
    
    buys = []
    remain = m
    while h:
        roi, idx = heappop(h)
        
        cnt = 0
        while stocks[idx][i] < 
        