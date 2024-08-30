from sys import stdin

h = len(bin(1000000))-2 

leafIdx = 2**h
tree = [0 for _ in range(2**(len(bin(1000000))-1))]

def update(idx,val):
    
    treeIdx = leafIdx + idx
    tree[treeIdx] = val
    
    while treeIdx > 1:
        treeIdx = treeIdx // 2
        tree[treeIdx] = tree[treeIdx*2] + tree[treeIdx*2+1]

def search(val):
    idx,acc = 1,0
    # print("val :", val)
    while idx < leafIdx:
        left = idx*2
        # print('idx : ', idx, 'left : ', left, 'acc : ', acc, 'tree[left] : ', tree[left])
        if acc + tree[left] >=  val:
            idx = left
        else:
            idx = left + 1
            acc += tree[left]
    return idx
    
n = int(stdin.readline())

for _ in range(n):
    cmd = list(map(int,stdin.readline().split()))
    
    if cmd[0] == 1:
        tmp =search(cmd[1]) 
        update(tmp-leafIdx, tree[tmp] - 1)
        # print("cmd1: ", tmp -leafIdx)
        print(tmp-leafIdx)
    elif cmd[0] == 2:
        update(cmd[1], tree[leafIdx+cmd[1]] + cmd[2])
        # print("rt : ", tree[1])
    
    
