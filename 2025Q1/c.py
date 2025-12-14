from sys import stdin

K = [
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],],
    [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
]
sumCacheK= [
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
]

def doubleVec(x):
    return [x_ * 2 for x_ in x]

def sumVec(x, y):
    return [x_ + y_ for x_, y_ in zip(x, y)]

def diffVec(x, y):
    return [x_ - y_ for x_, y_ in zip(x, y)]

transPos = [
    [int(3-j == i) for i in range(4)] for j in range(4)
]
# print(doubleVec([1,2,3,4]))
# print(sumVec([1,2,3,4], [4,3,2,1]))

for i in range(1,30):
    before = K[i]
    new = []
    for j in range(4):
        tmp = sumVec( doubleVec(before[j]) , K[1][j])
        
        if bin(j).count('1') % 2 ==0:
            tmp = sumVec(tmp, sumVec(before[1], before[2]))
        else:
            tmp = sumVec(tmp, sumVec(before[0], before[3]))
        
        new.append(tmp)
        
    tmp = sumVec(
        sumVec(new[0], new[1]), sumVec(new[2], new[3])
    )
    _sumCache = []
    for j in range(4):
        _sumCache.append(diffVec(tmp, new[j]))
    
    sumCacheK.append(_sumCache)
    K.append(new)

sum_k = [sum(__k[0])for __k in K]

# for i in range(1, 31):
#     print(f"{i} : ", K[i], sum_k[i], sumCacheK[i])



# print([ __k if 2 == __k.count(min(__k)) else None  for __k in __cache.keys()])
# print(_cache.keys())
def find(vec, k):   
    new = vec[:]
    min_val = min(vec)
    if vec.count(min_val) > 1:
        max_idx = vec.index(max(vec))
        min_idx = 3 - max_idx
    else:
        min_idx = vec.index(min_val)
    
    # base = K[k-1]
    # for i in range(4):
    #     if i == min_idx:
    #         continue
    #     new = diffVec(new, base[i])
    # print(new, sumCacheK[k-1][min_idx])
    new = diffVec(new, sumCacheK[k-1][min_idx])
    
    if any([n < 0 for n in new]):
        return [-1,[]]
    
    return [min_idx, new]

trans_table = [[0,0], [0,1], [1,0], [1,1]]
def trans(idx):
    return trans_table[idx]


twosqare = [ 1<<i for i in range(31)]

def sol():
    inp = list(map(int, stdin.readline().split()))
    # inp = rand_input()
    
    k = inp[0]
    v = inp[1:] 
    pos = [0,0]
    
    # print(f"input : {inp}")        
    
    if sum(v) != sum_k[k]:
        return[-1,-1]
    
    for _k in range(k, 0, -1):
            
        if v.count(sum_k[_k-1]) == 3: 
            idx = v.index(max(v))
            if v[idx] - 1 != sum_k[_k-1]:
                return [-1, -1]
            else:
                offset = [twosqare[_k-1]  -1, twosqare[_k-1] -1]
                pos = sumVec(pos, sumVec(trans(3-idx), offset))
                # print(f"pos : {pos}")
                return pos
        
        
        _idx, v = find(v, _k)
        if _idx < 0:
            return[-1, -1]
        
        pos = sumVec(pos , [t * twosqare[_k-1] for t in trans(_idx)])
        v = diffVec(v, transPos[_idx] )
        if any([_v < 0 for _v in v]):
            return [ -1, -1]
        # print(_idx,v, pos)
    
    # rev = F_dp(k, pos[0], pos[1])
    # print(rev, inp)
    # if inp[1:] != rev:
    #     print(inp)
    #     print(f"v:{inp[1:]} == {F_dp(k, pos[0], pos[1])}")
    # #     exit(1)
    # if sum(v) != 1:
    #     return [-1,-1]
    return pos

# print(sol())
ans = []
for _ in range(int(stdin.readline())):
    ans.append(sol())

for a in ans:
    print(f"{a[0]} {a[1]}")
    