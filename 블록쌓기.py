from sys import stdin
import random
prime = 1000000007

w, h = map(int ,stdin.readline().split())
cases = [1, 1, 2]
for i in range(3, w+1):
    cases.append((cases[i-1] + cases[i-2]+ cases[i-3]) % prime)
def calcCase(n):
    ans = 1
    cnt = 0
    for _ in range(w):
        # print(bin(n), cnt)
        if n & 1:
            cnt += 1
        else:
            ans *= cases[cnt]
            ans %= prime
            cnt = 0
        n >>= 1
    return (ans * cases[cnt]) % prime if cnt else  ans

def canStack(down, up):
    # print(bin(down), bin(up))
    # if up == 0:
    #     return False, up
    find = False
    for i in range(w):
        upbit, downbit = up & (1 << i), down & (1 << i)

        if upbit and not downbit:
            try:
                beforeupbit, afterupbit = up & (1 << (i-1)), up & (1 << (i+1))
                beforedownbit, afterdownbit = down & (1 << (i-1)), down & (1 << (i+1))  
                if find or not (beforeupbit and beforedownbit and afterupbit and afterdownbit) :
                    return False, up
                find = True
                up  &= ~ (1 << i)
                up  &= ~ (1 << i-1)
                up  &= ~ (1 << i+1)

            except:
                return False, up
        elif upbit and downbit:
            find = False
        if not upbit and downbit:
            find = False
    return True, up

fullcases = [calcCase(i) for i in range(2**w)]

# row : down
# col : up
stackTable = [[0 for _  in range(2**w)]for _ in range(2**w)]

# def makeRand():
#     return round(random.random() * 10000) % (2**w)

# for _ in range(10):
#     print(canStack(makeRand(), makeRand()))

for i in range(2**w):
    for j in range(2**w):

        flag , tmp = canStack(i, j)
        if flag:
            stackTable[i][j] = calcCase(tmp)

# for (idx,v) in enumerate(stackTable):
#     print(bin(idx), v)

ans = [0 for _ in range(2**w-1)] + [1]

for i in range(h):
    next = [0 for _ in range(2**w)]

    for j in range(2**w):
        for k in range(2**w):
            next[k] += (stackTable[j][k] * ans[j]) % prime
            next[k] %= prime
    # print(next)
    ans = next

print(sum(ans) % prime)