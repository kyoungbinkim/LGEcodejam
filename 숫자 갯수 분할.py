def parseK(k):
    parsed = []
    if k <= 11:
        tmp = [6,3,1,1]
        idx = 3
        
        while k >= tmp[idx]:
            k -= tmp[idx]
            parsed.append(tmp[idx])
            idx -= 1
        if k > 0:
            parsed.append(k)
    else:
        parsed.append(1)
        k -= 1
        
        while k >= parsed[-1] * 2:
            k -= parsed[-1] * 2
            parsed.append(parsed[-1] * 2)
        if k:
            parsed += parseK(k)
    return parsed

def test():
    for i in range(1, 33):
        print(i, parseK(i))

test()