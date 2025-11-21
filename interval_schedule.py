def max_meetings(people):
    events = []
    
    # 1. 모든 시작/종료 시간을 이벤트로 변환
    for i, (start, end) in enumerate(people):
        events.append((start, 1))   # 시작: +1
        events.append((end, -1))    # 종료: -1
    
    # 2. 시간순 정렬 (같은 시간이면 종료가 먼저)
    events.sort(key=lambda x: (x[0], x[1]))
    
    # 3. Sweep line으로 동시 재실 인원 추적
    max_overlap = 0
    current_people = 0
    
    for time, delta in events:
        current_people += delta
        max_overlap = max(max_overlap, current_people)
    
    return max_overlap