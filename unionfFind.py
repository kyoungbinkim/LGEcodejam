
p = [i for i in range(10)]

def findParent(x):
    if p[x] != x:
        p[x] = findParent(p[x])
    return p[x]

def union(a, b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b