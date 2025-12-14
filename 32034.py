from sys import stdin
from collections import deque

def updateQueue(q):
    cur = ['H', 0]
    
    while q and q[-1][0] == 'H':
        cur[1] += q.pop()[1]
    if cur[1]:
        q.append(cur)
    return q

def sol():
    n = int(stdin.readline())
    logs, ans = deque(), 0
    strs = stdin.readline().rstrip()
    
    for i,c in enumerate(strs):
        # print(strs, logs, ans , c , i)
        if len(logs) == 0:
            logs.append([c,1])
            continue
        
        cur = [logs.pop()]
        if c == cur[-1][0]:
            cur[-1][1] += 1
            logs.append(cur[-1])
            continue
        elif c == 'H':
            if cur[-1][1] % 2 == 0:
                ans += cur[-1][1] // 2
                logs.append(['H', cur[-1][1]])
            elif len(logs) > 1 and logs[-1][1] % 2 == 0 and logs[-2][1] % 2:
                for _ in range(2):
                    cur.append(logs.pop())
                ans += cur[1][1] //2 
                ans += sum([x[1] for x in cur]) // 2
                logs.append(['H', sum([x[1] for x in cur])])
            else:
                logs.append(cur[-1])
        elif c == 'T':
            logs.append(cur[-1])
            
        logs.append([c, 1])
        logs = updateQueue(logs)
    
    # print('\n', logs, '\n')
    while logs:
        tmp = logs.pop()
        if tmp[0] == 'H':
            continue
        if tmp[1] % 2:
            cur = [tmp]
            if len(logs) > 1 and logs[-1][1] % 2 == 0 and logs[-2][1] % 2:
                for _ in range(2):
                    cur.append(logs.pop())
                ans += cur[1][1] // 2 
                ans += sum([x[1] for x in cur]) // 2
            else:
                print(-1)
                return
        else:
            ans += tmp[1] // 2
        logs = updateQueue(logs)
    print(ans)

for _ in range(int(stdin.readline())):
    sol()                    
    
