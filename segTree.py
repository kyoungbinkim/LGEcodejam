from sys import stdin

n = int(stdin.readline())
leafs = [i for i in range(1,n+1)]
height = len(bin(n)) -2
leafsCnt = 2**height

tree = [0 if i<leafsCnt or i-leafsCnt >= len(leafs) else leafs[i-leafsCnt] for i in range(2**(height+1))]

def init(node, start, end): 
    if start == end :
        tree[node] = leafs[start]
        return tree[node]
    else :
        ## 여기 논리를 구현해야함 .
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]


def find(node, start, end, left, right) :
    
    if left > end or right < start :
        return 0

    if left <= start and end <= right :
        return tree[node]
 
    ## 밑은 논리에 따라 바뀔 수 있따.
    return find(node*2, start, (start+end)//2, left, right) + find(node*2 + 1, (start+end)//2+1, end, left, right)
 
## TODO 리프부터 올라가는 것을 ㅗ바꿔
def update(node, start, end, index) :
 
    if index < start or index > end :
        return
 
    tree[node] += diff
    
    if start != end :
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)

def update2(node, index):
    
    
    tree[node] = leafs[index]
    
    while node > 1:
        node = node // 2
        
        ## update 로직
        tree[node] = tree[node*2] + tree[node*2+1]

print(tree)