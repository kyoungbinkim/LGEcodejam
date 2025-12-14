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
    nexts = [False for _ in range(3)]

    # R0G1, R0B2, G1B2
    diff = [False for _ in range(4)]
    flags = [False for _ in range(3)]

    firEnd= [s[0]!=s[1], s[-1] != s[-2]]

    for i, c in enumerate(s):
        flags[cmap[c]] = flags[cmap[c]] if flags[cmap[c]] != None else False
        if c != before:
            
            if 0 < i < slen:
                diff[cmap[c] + cmap[before]] = True
                if i < slen-1 and before == s[i+1]:
                    flags[cmap[before]] = True
                elif i < slen-1 and c != s[i+1]:
                    nexts[cmap[c]] = True
            

            before = c
        else:
            cnts[cmap[c]] += 1
    # print(flags, )
    # print(nexts,)
    ans = []

    for i in range(3):
        if flags[i] == True:
            ans.append([cnts[j] + (j==i)*2   for j in range(3)])

        if nexts[i]:
            for j in range(2):
                tmp = cnts.copy()
                tmp[(i+j + 1)%3] += 1
                ans.append(tmp)
            
    if sum(nexts) == 0 and sum(flags) == 0:
        if firEnd[0]:
            tmp = cnts.copy()
            tmp[cmap[s[1]]] += 1
            ans.append(tmp)
        if firEnd[1]:
            tmp = cnts.copy()
            tmp[cmap[s[-2]]] += 1
            ans.append(tmp)

    ans.append(cnts)
    if diff[1] :
            ans.append([cnts[0]+1, cnts[1]-1, cnts[2]])
            ans.append([cnts[0]-1, cnts[1]+1, cnts[2]])
    if diff[2] :
            ans.append([cnts[0]-1, cnts[1], cnts[2]+1])
            ans.append([cnts[0]+1, cnts[1], cnts[2]-1])
    if diff[3] :
            ans.append([cnts[0], cnts[1]-1, cnts[2]+1])
            ans.append([cnts[0], cnts[1]+1, cnts[2]-1])


    # if diff[1] :
    #     ans.append([cnts[0]+1, cnts[1]-1, cnts[2]])
    #     ans.append([cnts[0]-1, cnts[1]+1, cnts[2]])
    # elif diff[2] :
    #     ans.append([cnts[0]-1, cnts[1], cnts[2]+1])
    #     ans.append([cnts[0]+1, cnts[1], cnts[2]-1])
    # elif diff[3] :
    #     ans.append([cnts[0], cnts[1]-1, cnts[2]+1])
    #     ans.append([cnts[0], cnts[1]+1, cnts[2]-1])
        
    return ans, flags

def calcScore(x,y,z):
    score = 0
    for i,j,k in permutations(range(3)):
        x[i] = max(0, x[i])
        y[j] = max(0, y[j])
        z[k] = max(0, z[k])
        score += x[i] * y[j] * z[k]

    # print(score)
    return score


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

    # print(cx)
    # print(cy)
    # print(cz)

    ans = 0
    for x in cx:
        tmp = 0
        for y in cy:
            for z in cz:
                ans = max(ans, calcScore(x,y,z))
    print(ans)


    # ans = 0
    # for x,y,z in permutations(range(3)):
    #     # print(x,y,z)
    #     ans = max(
    #         min(cx[x] , lx) * \
    #             min(cy[y] , ly) *\
    #                  min(cz[z] , lz), ans)
        
    # print(ans)

