from sys import stdin

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
sum_board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        sum_board[i][j] = sum_board[i][(j+1) % n] + board[i][j]

for b in sum_board:
    print(b)

total = sum([sum_board[i][0] for i in range(n)])

ans = float('inf')


5 4 3 2 1