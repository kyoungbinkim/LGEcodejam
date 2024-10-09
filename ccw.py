def ccw(A, B, C):
    """
    세 점이 반시계 방향인지 시계 방향인지 판별하는 함수.
    
    AB-> 와 AC->  외적을 통해 판별
    return: 1 (반시계 방향), -1 (시계 방향), 0 (일직선)
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    
    cross_product = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if cross_product > 0:
        return 1  # 반시계 방향
    elif cross_product < 0:
        return -1  # 시계 방향
    else:
        return 0  # 일직선

# 예시 사용
x1, y1 = 0, 0
x2, y2 = 1, 1
x3, y3 = 2, 0

result = ccw([x1, y1], [x2, y2], [x3, y3])
if result == 1:
    print("반시계 방향")
elif result == -1:
    print("시계 방향")
else:
    print("일직선")
