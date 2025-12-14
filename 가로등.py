from sys import stdin

def sol():
    n = int(stdin.readline())
    
    xset, yset = set(), set()
    
    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        xset.add(x)
        yset.add(y)
    
    if len(xset) * len(yset) == n:
        print('BALANCED')
    else:
        print('NOT BALANCED')
   
for _ in range(int(stdin.readline())):
    sol()