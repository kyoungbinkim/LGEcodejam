from sys import stdin

n = int(stdin.readline())
leafs = [i for i in range(1,n+1)]
height = len(bin(n)) -2
leafsCnt = 2**height

tree = [0 if i<leafsCnt or i-leafsCnt >= len(leafs) else leafs[i-leafsCnt] for i in range(2**(height+1))]

print(tree)