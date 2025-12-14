from sys import stdin

n = int(stdin.readline())
zeros = set(range(n))
ones, twos = (set() for _ in range(2))
stars=[tuple(map(int, stdin.readline().split())) for _ in range(n)]

s,c = 0,0 # 별, 방문 숫자

while len(twos) < n:    
    tmp = None
    for idx in ones:
        if stars[idx][1] <= s:
            c += 1
            s += 1
            
            ones.remove(idx)
            twos.add(idx)
            tmp = -1
            break
    
    if tmp is not None:
        continue
    
    for idx in zeros:
        if stars[idx][1] <= s:
            c += 1
            s += 2
            
            zeros.remove(idx)
            twos.add(idx)
            tmp = -1
            break
        elif stars[idx][0] <= s:
            if tmp is None or stars[tmp][1] < stars[idx][1]:
                tmp = idx
    
    if tmp == None:
        print("Too Bad")
        exit()
    elif tmp > -1:
        c += 1
        s += 1
            
        zeros.remove(tmp)
        ones.add(tmp)
print(c)