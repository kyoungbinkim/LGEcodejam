# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
from heapq import heappush, heappop, heapify


def input_data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	infos = [list(map(int, readl().split())) for _ in range(M)]
	return N, M, infos

sol = -1

# 입력받는 부분
N, M, infos = input_data()
b = [[float("inf") for _ in range(N)] for _ in range(N)]
ans = [[None for _ in range(N)] for _ in range(N)]
for i,j,d in infos:
	b[i-1][j-1] = b[j-1][i-1] = d

h = []
def dijkstra(startIdx):
	dp = [float('inf') for _ in range(N)]
	dp[startIdx] = 0
	
	for endIdx in range(N):
		if dp[endIdx] == float('inf') and b[startIdx][endIdx] != float('inf'):
			heappush(h, (b[startIdx][endIdx], startIdx, endIdx))
	
	while h:
		w, s, e = heappop(h)
		
		# if dp[e] != float('inf'):
		# 	continue
		
		if dp[e] > dp[s] + b[s][e]:
			dp[e] = dp[s] + b[s][e]
		
		for endIdx in range(N):
			if dp[endIdx] == float('inf') and b[e][endIdx] != float('inf'):
				heappush(h, (dp[e] + b[e][endIdx], e, endIdx))
		
		# if float('inf') not in dp:
		# 	break
		print(s,e, dp)
		
	for i in range(N):
		ans[i][startIdx] = ans[startIdx][i] = dp[i]

for idx in range(N):
	dijkstra(idx)

	for l in ans:
		print(l)
	print()

# 여기서부터 작성


# 출력하는 부분
print(sol)
