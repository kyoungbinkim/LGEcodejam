from sys import stdin

source = stdin.readline().removesuffix('\n')
target = stdin.readline().removesuffix('\n')
lent = len(target)

startIdx = set()
start = {}

pi = [0 for _ in range(lent)]

i = 0
for j in range(1, lent):
    while i > 0 and target[i] != target[j]:
        i = pi[i-1]
    if target[i] == target[j]:
        i += 1
        pi[j] = i
print(pi)

ret = []
i=0
for j in range(len(source)):
    while i > 0 and source[j] != target[i]:
        i = pi[i-1]
    if source[j] == target[i]:
        if i == lent-1:
            ret.append(j-lent+2)
            i = pi[i]
        else:
            i += 1

# print(len(ret))
for i in ret:
    print(i)    
    