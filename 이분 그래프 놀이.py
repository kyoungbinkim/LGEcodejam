from sys import stdin

a = {
    'a' : 1,
    'b' : None
}
print(a.keys())

def sol():
    n,m,k = map(int, stdin.readline().split())
    
    degA = [0 for _ in range(n)]
    degB = [0 for _ in range(m)]
    edges = []
    
    degCnt = {
        'a' : {
            0 : n
        },
        'b' :  {
            0 : m
        }
    }
    
    for _ in range(k):
        a,b = map(lambda x: int(x)-1, stdin.readline().split())
        
        degCnt['a'][degA[a]] -= 1
        degCnt['b'][degB[b]] -= 1
        if degCnt['a'][degA[a]] == 0:
            degCnt['a'].pop(degA[a])
        
        if degCnt['b'][degB[b]] == 0:
            degCnt['b'].pop(degB[b])
        
        
        degCnt['a'][degA[a]+1] = degCnt['a'].get(degA[a]+1, 0) + 1
        degCnt['b'][degB[b]+1] = degCnt['b'].get(degB[b]+1, 0) + 1
        
        degA[a] += 1
        degB[b] += 1
        edges.append((a,b))
    
    print(degA, degB, degCnt, edges)
    
    

for _ in range(int(stdin.readline())):
    sol()