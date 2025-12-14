from sys import stdin

N, K = map(int, stdin.readline().split()) 


items = []
for _ in range(N):
    items.append(tuple(map(int, stdin.readline().split())))

evnts = []
for s, e, p, d in items:
    evnts.append((s, 1, p, d, s, e))   
    evnts.append((e + 1, -1, p, d, s, e))  
    
evnts.sort()

total_cost = 0 
sum_d = 0  
cnt = 0     
ans = float('inf')

i = 0
before_day = None

while i < len(evnts):
    now_day = evnts[i][0]
    
    if before_day is not None and before_day < now_day:
        if cnt >= K:
            cost_at_prev_day = total_cost - sum_d * (now_day - 1 - before_day)
            ans = min(ans, cost_at_prev_day)

        total_cost -= sum_d * (now_day - before_day)
    
    
    events_to_process = []
    while i < len(evnts) and evnts[i][0] == now_day:
        events_to_process.append(evnts[i])
        i += 1

    for _, typ, p, d, s, e in events_to_process:
        if typ == 1:
            total_cost += p
            sum_d += d
            cnt += 1
        elif typ == -1:
            cost_at_end_day = p - d * (now_day - 1 - s) 
            total_cost -= cost_at_end_day
            sum_d -= d
            cnt -= 1

    if cnt >= K:
        ans = min(ans, total_cost)
        
    before_day = now_day
    
print(ans if ans != float('inf') else -1)