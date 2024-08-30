

def FloydWarShall():
	for i in range(N):
		for s in range(N):
			for e in range(N):
				if b[s][i] == float('inf') or b[i][e] == float('inf'):
					continue
				b[s][e] = min(b[s][e], b[s][i] + b[i][e])