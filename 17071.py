from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)



# n, k = map(int, stdin.readline().split())

import random
n,k = random.randint(0,500_000), random.randint(0,500_000)
print(n,k)

global is_find
is_find = n == k
def dfs(s,d,depth, max_depth, visit):
    global is_find
    
    if s == d and depth == max_depth:
        is_find = True
        return
    
    if is_find or depth >= max_depth or s > 500_000 or s<0 or s in visit[depth]:
        return
    visit[depth].add(s)

    dfs(s+1, d, depth+1, max_depth, visit)
    dfs(s-1, d, depth+1, max_depth, visit)
    dfs(2*s, d, depth+1, max_depth, visit)

i = 1
visit = [set([n])]
while not is_find and k <= 500_000:
    k += i
    
    next_set = set()
    
    if k-1 in visit[-1]
    
    i += 1
    print(k, "...",i)
print(i-1 if is_find else -1)




'''
k + i(i+1) // 2  == n + F(i)

k - n = F(i) - i(i+1) //2


F(i):
    k : 2배수 수
    a : +1 갯수
    b : -1 갯수
    
    
    


n

n-1  n+1  2*n

n-2 n n+2  2n-1 2n+1      2n-2 2n+2    4n


n-3 n-1  n+1 n+3    2n-2 2n  2n+2    2n-3 2n-1  2n+1 2n+3    4n-1 4n+1
2n-4 2n 2n+4    4n-2 4n+2  4n-4 4n+4 8n 




(승수k, +갯수a, -갯수b) 

13

1의 갯수으로 만드는 법

2^k n


'''