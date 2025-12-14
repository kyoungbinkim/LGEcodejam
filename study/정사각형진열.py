from sys import stdin
from collections import deque

n = int(stdin.readline())
flags = [False for _ in range(n)]
sList = list(map(int, stdin.readline().split()))
posList = [[sList[0], 0, sList[0]*2, 0]]

for (idx, s) in enumerate(sList[1:]):
    # if posList[-1][2] * 1.5 <= s:
    #     posList.append([s, 0, s*2, idx+1])
    #     continue
    pos = [s, 0, -float('inf'), idx+1]

    for before in posList:
        if before[0] < s:
            start = before[2] + before[0] - s
            end = before[2] + before[0] + s
        elif before[0] > s:
            start = before[2] - before[0] + s
            end = before[2] - before[0] + 3 * s
        else:
            start = before[2]
            end = before[2] + s * 2

        if end > pos[2]:
            pos = [s, start, end, idx+1]
    posList.append(pos)
posList.sort(key=lambda x: x[0], reverse=True)        
# print(posList)

flags[posList[0][3]] = True
tmp = [(posList[0][1], posList[0][2])]

ans = [str(posList[0][3]+1)]
for (s, start, end, idx) in posList[1:]:
    if len(tmp) == 1:
        before = tmp[0]
        if before[0]  <= start and end <= before[1]:
            continue

        if end < before[0]:
            tmp = [(start, end)] + tmp
        elif start > before[1]:
            tmp = tmp + [(start, end)]
        else:
            tmp[0] = (min(before[0], start), max(before[1], end))
        flags[idx] = True
        ans.append(str(idx+1))
    else:
        if tmp[0][0] > end:
            tmp = [(start, end)] + tmp
            flags[idx] = True
            ans.append(str(idx+1))
            continue

        for (i, (before, after)) in enumerate(zip(tmp, tmp[1:]+[(float('inf'), float('inf'))])):
            # print(before, after, (start, end))
            if before[0] > end:
                continue
                
            if after[1]  < start:
                break
            
            if before[0] <= start and end <= before[1]:
                break
 
            if before[1] < start and end < after[0]:
                tmp = tmp[:i+1] + [(start, end)] + tmp[i+1:]
                flags[idx] = True
                ans.append(str(idx+1))
                break

            if end >= after[0] and start <= before[1]:
                tmp[i] = (min(before[0], start),max(end, after[1]))
                tmp.pop(i+1)
                flags[idx] = True
                ans.append(str(idx+1))
                break
            elif start <= before[1]:
                # print(start, end, before, after)
                # print("??")
                tmp[i] = (min(before[0], start), max(before[1], end))
                flags[idx] = True
                ans.append(str(idx+1))
                break
            elif after[1] >= end >= after[0]:
                tmp[i+1] = (min(after[0], start), max(after[1], end))
                flags[idx] = True
                ans.append(str(idx+1))
                break
    # print(tmp)

# print(flags)
ans.sort(key = lambda x : int(x))
print(' '.join(ans))
# for (idx, f) in enumerate(flags):
#     if f:
#         print(idx+1, end=' ')
# print()