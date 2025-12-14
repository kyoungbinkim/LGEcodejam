from sys import stdin

N, K = map(int, stdin.readline().split())
items = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

evnts = []
for s, e, p, d in items:
    evnts.append((s, 1, p, d, s))   
    evnts.append((e, -1, p, d, s))  
    
evnts.sort()


total_cost = 0 
sum_d = 0    
cnt = 0
ans = float('inf')
end = []
i = 0
before_day = None
while i < len(evnts):
    now_day = evnts[i][0]
    
    if before_day:
        total_cost -= sum_d * (now_day-before_day)
    if cnt >= K and now_day-before_day:
        if end and now_day-before_day == 1:
            tmp = sum([p - d*(e - s) for e,_,p,d,s in end])
            ans = min(ans, total_cost+sum_d + tmp)
        else:
            ans = min(ans, total_cost+sum_d)
    end, sum_p = [], 0

    
    while i < len(evnts) and evnts[i][0] == now_day:
        _idx, typ, p, d, s = evnts[i]
        if typ == 1:
            total_cost += p
            sum_d += d
            cnt += 1
        elif typ == -1:
            end.append([_idx, typ, p, d, s])
        i+=1
    
    if cnt >= K :
        ans = min(ans, total_cost)
    # print(f"total cost : {total_cost} cnt : {cnt}. {_idx}")
    
    for e,_,p,d,s in end:
        sum_d -= d
        total_cost -= p - d*(e - s)
        cnt -= 1
    
    # if len(end) and i < len(evnts)-1  and now_day+1 != evnts[i+1][0]:
    #     if cnt >= K :
    #         ans = min(ans, total_cost - sum_d)
        
    before_day = now_day
print(ans if ans != float('inf') else -1)
