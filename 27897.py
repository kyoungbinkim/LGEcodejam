from sys import stdin

n, l = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

ans, update, idxMap = 0, 0, {}


for i,num in enumerate(nums):
    
