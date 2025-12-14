from sys import stdin
from collections import deque

N = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
cnts = [a.count(i) for i in range(4)]