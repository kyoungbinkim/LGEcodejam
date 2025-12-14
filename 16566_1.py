from sys import stdin
from collections import deque

INF = 4_000_001

n,m,k = map(int, stdin.readline().split())

cards = list(map(int, stdin.readline().split()))
reds = list(map(int, stdin.readline().split()))
blues = []

cards.sort()

class Node:
    def __init__(self, left, right, val=None):
        self.parent=None
        self.left = left
        self.right = right
        self.maxV = max(left.maxV, right.maxV)  if val is None else val
        self.minV = min(left.minV, right.minV)  if val is None else val
    
