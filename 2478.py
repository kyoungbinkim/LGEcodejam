from copy import deepcopy
from sys import stdin
from collections import deque

import random


n  = 10

def chunck_list(l):
    ret = [[l[0], l[0]]]
    
    for e in l[1:]:
        if abs(ret[-1][1]- e) == 1:
            ret[-1][1] = e
        else:
            ret.append([e,e])
    return ret

def updateList(ans):
    ret = [ans[0]]
    for a in ans[1:]:
        if a[0] - ret[-1][1] == 1:
            ret[-1][1] = a[1]
        else:
            ret.append(a)
    return ret

def flip(seq):
    
    l = chunck_list(seq)
    if len(l) == 1 or len(l) > 4:
        return (None, None, None)
    p,q = float('inf'), -float('inf')
    
    for i in range(len(l)):
        ans = deepcopy(l)
        if ans[i][0] > ans[i][1]:
            ans[i][0],ans[i][1] = ans[i][1], ans[i][0]

            ans = updateList(ans)
            # print(ans)
            
            if any([a>b for a,b in ans]):
                continue
            
            if len(ans) == 2:
                p,q = seq.index(l[i][0]), seq.index(l[i][1])
                return p,q, ans
    
    for i in range(len(l) - 1):
        ans = deepcopy(l)
        ans[i][0],ans[i][1] = ans[i][1], ans[i][0]
        ans[i+1][0],ans[i+1][1] = ans[i+1][1], ans[i+1][0]
        ans[i],ans[i+1] = ans[i+1], ans[i]
        ans = updateList(ans)
        
        if any([a>b for a,b in ans]):
                continue
        
        if len(ans) == 2:
            p = seq.index(l[i][0])
            q = seq.index(l[i+1][1])
            return p,q, ans

    return (None, None, None)
    
def k_push(seq, k):
    return seq[k:] + seq[:k]

def pq_flip(seq, p, q):
    seq[p:q+1] = seq[p:q+1][::-1]
    return seq

def test(n=15 , verbose=False):
    ans = list(range(1,n+1))
    k = [random.randrange(1,n) for _ in range(2)]
    ans = k_push(ans, k[0])
    p = random.randrange(0,n-1)
    q = random.randrange(p+1, n)
    ans = pq_flip(ans, p, q)
    # ans = k_push(ans, k[1])
    
    if verbose:
        print(*ans)
        print(f"chunk list : {chunck_list(ans)}")
        print(f"k : {k}")
        print(f"flip : {flip(ans)}")
        print(f"p:{p}, q:{q}")
    
    ans = k_push(ans, k[1])
    if verbose:
        print(*ans)
        print("\n\n")
    return ans
    
    
def sol(n, l):
    
    for k2 in range(1, n):
        seq = l[-k2:] + l[:-k2]
        
        p,q,ans = flip(seq)
        
        if p == None or q==None:
            continue
        # print(f"seq : {seq}")
        seq = pq_flip(seq,p, q)
        # print(f"""              seq : {seq}
        #       k : {ans[-1][-1]}
        #       p,q : {p+1}, {q+1}
        #       k : {k2}
        #       ans : {ans}
        #       """)
        print(ans[-1][-1])
        print(f"{p+1} {q+1}")
        print(f"{k2}")
        
        return ans[-1][-1], p+1, q+1, k2

for _ in range(0):
    n = 15
    t = test(n=n)
    
    print(_,'\n', *t)
    
    k1, p,q, k2 = sol(n,t)
    
    seq = list(range(1, n+1))
    
    seq = k_push(seq, k1)
    seq = pq_flip(seq, p-1, q-1)
    seq = k_push(seq, k2)
    print(*seq, '\n\n')
    
    if seq != t:
        break




n = int(stdin.readline())
l = list(map(int, stdin.readline().split()))
sol(n, l)



'''
15
13 12 5 6 7 8 9 10 11 4 3 2 1 15 14

8 9 10 1 2 3 4 5 6 7
8 9 2 1 10 3 4 5 6 7
9 2 1 10 3 4 5 6 7 8




15
12 11 10 9 8 7 1 2 3 4 5 6 15 14 13
'''