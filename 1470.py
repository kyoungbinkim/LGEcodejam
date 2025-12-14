from sys import stdin

n,l = map(int, stdin.readline().split())

upper, same = 0, []
stand = list(map(int, stdin.readline().split()))
stand[0] += l



for _ in range(n-1):
    tmp = list(map(int, stdin.readline().split()))
    if tmp[0] > stand[0]: upper += 1
    elif tmp[0] == stand[0]: 
        pass
same.sort(reverse=True, key=lambda x: (int(x[2] > stand[2]), x[1]))

print(same)