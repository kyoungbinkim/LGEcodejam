from sys import stdin
from itertools import permutations

cmap = {
    'R': 0,
    'G': 1,
    'B': 2
}

t = int(stdin.readline())

def calcRGB(s):
    before, slen = None, len(s)
    cnts = [0 for _ in range(3)]
    flags = [None for _ in range(3)]

    for i, c in enumerate(s):
        flags[cmap[c]] = flags[cmap[c]] if flags[cmap[c]] != None else False
        if c != before:
            if i < slen-1:
                if before == s[i+1]:
                    flags[cmap[before]] = True
            before = c
        else:
            cnts[cmap[c]] += 1

    ans = [0 for _ in range(3)]

    for i in range(3):
        if flags[i] == None:
            ans[i] = cnts[i]
        elif flags[i] == False:
            ans[i] = cnts[i] + 1
        else:
            ans[i] = cnts[i] + 2
    return ans, flags

for _ in range(t):
    nx,ny,nz = map(int, stdin.readline().split())
    sx = stdin.readline().rstrip()
    sy = stdin.readline().rstrip()
    sz = stdin.readline().rstrip()

    lx, ly, lz = len(sx)-1, len(sy)-1, len(sz)-1

    # print(calcRGB(sx), calcRGB(sy), calcRGB(sz))

    cx, fx = calcRGB(sx)
    cy, fy = calcRGB(sy)
    cz, fz = calcRGB(sz)

    ans = 0
    for x,y,z in permutations(range(3)):
        # print(x,y,z)
        ans = max(
            min(cx[x] , lx) * \
                min(cy[y] , ly) *\
                     min(cz[z] , lz), ans)
        
    print(ans)

