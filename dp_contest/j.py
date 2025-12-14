from sys import stdin
from collections import deque

N = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
cnts = [a.count(i) for i in range(4)]

# hit, cnt
cur,next = {
    tuple(cnts): [1, [0,1]]
        }, {}

def gcd(a,b):
    if b==0 or a==0:
        return a+b
    
    return gcd(a%b, b) if a>b else gcd(b%a, a)

def f_mul(a,b):
    tmp = [a[0]*b[0], a[1]*b[1]]
    g = gcd(tmp[0], tmp[1])
    return [tmp[0] // g, tmp[1]//g]

#[분자, 분모]
def f_add(a,b):
    tmp = [a[0]*b[1]+b[0]*a[1], a[1]*b[1]]
    g = gcd(tmp[0], tmp[1])
    return [tmp[0] // g, tmp[1]//g]
    

while cur:
    for k in cur.keys():
        # print(k)
    
        hit_cnt = f_add(f_mul([N,N-k[0]], [cur[k][0],1]), cur[k][1])
        # hit_cnt = N / (N-k[0])  * cur[k][0] + cur[k][1]
        for i in range(1,4):
            if k[i] == 0:
                continue
            tmp = list(k)
            
            tmp[i]   -= 1
            tmp[i-1] += 1
            
            if next.get(tuple(tmp)):
                next[tuple(tmp)][0] += cur[k][0] 
                next[tuple(tmp)][1] = f_add(next[tuple(tmp)][1], hit_cnt)
            else:
                next[tuple(tmp)] = [cur[k][0],  hit_cnt]
    
    print(next)
    cur = next
    next = {}
    if len(cur) == 1 and (N,0,0,0) in cur.keys():
        ans = cur.pop((N,0,0,0))
        print(ans[1][0]/ (ans[0]*ans[1][1]))
        break
            
        
        
'''

1번  2번 1,0,1,0  2번 1 1 0 0 - 2 0 0 0
             
    1번  0,2,0,0   1 1 0 0 
     
    

0 1 1 1 (1) - 1 0 1 1 (1.5) - 1 1 0 1 (1.5) - 2 0 0 1 (3)
                                            - 1 1 1 0 (1.5)
                            - 1 0 2 0 (1.5) - 1 1 1 0 (1.5)
            - 0 2 0 1 (1)   - 1 1 0 1 (1.5) - 2 0 0 1 (3)
                                            - 1 1 1 0 (1.5)
                            - 0 2 1 0 (1)   - 1 1 1 0 (1.5)
                                            - 0 3 0 0 (1)
            - 0 1 2 0 (1)   - 1 0 2 0 (1.5) - 1 1 1 0 (1.5)
                            - 0 2 1 0 (1)   - 1 1 1 0 (1.5)
                                            - 0 3 0 0 (1)
                                            
                                            
            1, 1            1 1 0 1 - 2, 4.5
            1, 1            1 0 2 0 - 2, 4.5
            1, 1            0 2 1 0 - 2  4

'''