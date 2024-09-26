
all_position = set()
for _ in range(n):
    a,b = map(int, stdin.readline().split())
    all_position.add(a)
    all_position.add(b)

sorted_position = sorted(list(all_position))
position2idx = {v:i for i,v in enumerate(sorted_position)}