from sys import stdin

K = [
    [[0],[],[],[]],
    [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
]
sumCacheK= [
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
]

doubleVec   = lambda x: [_x*2 for _x in x]
sumVec      = lambda x,y: [_x+_y for _x,_y in zip(x,y)]
diffVec     = lambda x,y: [_x-_y for _x,_y in zip(x,y)]
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

memo = {}
def F_dp(K, x, y):
    def dp(k, x, y):
        key = (k, x, y)
        if key in memo:
            return memo[key]
        result = [0, 0, 0, 0]
        if k == 1:
            tile_map = {(0, 0): 3, (0, 1): 2, (1, 0): 1, (1, 1): 0}
            result[tile_map[(x, y)]] += 1
            return result
        half = 2 ** (k - 1)
        if x < half and y < half:
            quadrant = 0
        elif x < half and y >= half:
            quadrant = 1
        elif x >= half and y < half:
            quadrant = 2
        else:
            quadrant = 3
        tile_center = [3, 2, 1, 0]
        result[tile_center[quadrant]] += 1
        # Compute the results for the four quadrants
        if quadrant == 0:
            result0 = dp(k-1, x, y)
        else:
            result0 = dp(k-1, half-1, half-1)
        if quadrant == 1:
            result1 = dp(k-1, x, y-half)
        else:
            result1 = dp(k-1, half-1, 0)
        if quadrant == 2:
            result2 = dp(k-1, x-half, y)
        else:
            result2 = dp(k-1, 0, half-1)
        if quadrant == 3:
            result3 = dp(k-1, x-half, y-half)
        else:
            result3 = dp(k-1, 0, 0)
        for i in range(4):
            result[i] += result0[i] + result1[i] + result2[i] + result3[i]
        memo[key] = tuple(result)
        return tuple(result)
    return dp(K, x, y)

_cache = {}
for i in range(8):
    for j in range(8):
        _cache[F_dp(3,i,j)] = (i,j)

__cache = {}
for i in range(16):
    for j in range(16):
        __cache[F_dp(4,i,j)] = (i,j)

def find(vec, k):    
    new = vec
    min_idx = vec.index(min(vec))
    
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
    k = inp[0]
    v = inp[1:] 
    pos = [0,0]
    
    # print(f"input : {inp}")        
    
    if sum(v) != sum_k[k]:
        return[-1,-1]
    
    for _k in range(k, 0, -1):
        if _k == 3:
            _diff = _cache.get(tuple(v), None)
            if _diff:
                return sumVec(pos, _diff)
            else:
                return [-1, -1]
        elif _k ==4:
            _diff = __cache.get(tuple(v), None)
            if _diff:
                return sumVec(pos, _diff)
            else:
                return [-1, -1] 
            
        if v.count(sum_k[_k-1]) == 3: 
            idx = v.index(max(v))
            if v[idx] - 1 != sum_k[_k-1]:
                return [-1, -1]
            else:
                offset = [(1<<(_k-1))  -1, (1<<(_k-1))-1]
                pos = sumVec(pos, sumVec(trans(3-idx), offset))
                # print(f"pos : {pos}")
                return pos
        
        
        _idx, v = find(v, _k)
        if _idx < 0:
            return[-1, -1]
        
        pos = sumVec(pos,[t * (1<<(_k-1)) for t in trans(_idx)])
        v = diffVec(v,transPos[_idx] )
        if any([_v < 0 for _v in v]):
            return [ -1, -1]

        print(v, )
    if sum(v) != 1:
        return [-1,-1]
    return pos

# print(sol())
ans = []
for _ in range(int(stdin.readline())):
    ans.append(sol())

for a in ans:
    print(f"{a[0]} {a[1]}")
    