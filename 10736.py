from sys import stdin

from itertools import combinations

for i in range(1, 6):
    for j in range(i+1, 7):
        print(f"{(i)} xor {(j)} = {i^j}")
        
print(len(list(combinations(range(100),2))))




for n in range(3, 11):
    print(n)
    deg = [0 for _ in range(129)]
    
    dir = {i:set() for i in range(1, n+1)}
    
    for i in range(1,n):
        for j in range(i+1, n+1):
            dest = i^j
            deg[i] += 1
            deg[j] += 1
            deg[dest] += 1

            dir[i].add(dest)
            dir[j].add(dest)
            
    print(deg, dir)


def update(deg, dir, tar):
    
    
    for dest in dir[tar]:
        deg[dest] -= 1
    



def solve(n):
    s = list(range(1, n+1))
    
    
    for i in range(n, 0 ,-1):
        for nCi in combinations(s, i):
            tmp = set(s).difference(set(nCi))
            # print(nCi)
            for idx in range(i-1):
                for jdx in range(idx+1, i):
                    if nCi[idx] ^ nCi[jdx] in nCi:
                        break
                else:
                    continue
                break
                
            else:
                print(i)
                print(*nCi)
                return
                print(f"jdx == {jdx},  {i}")


for i in range(1, 11):
    print(f"\nans : {i}")
    solve(i)