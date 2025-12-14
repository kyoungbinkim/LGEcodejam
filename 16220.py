from sys import stdin
from collections import Counter

N = int(stdin.readline())
schedules = []

for _ in range(N):
    s,e = map(int, stdin.readline().split())
    
    schedules.append((s,1))
    schedules.append((e,-1))