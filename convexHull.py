'''
Graham's Scan 알고리즘
'''

def ccw(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    cp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if cp > 0:
        return 1  # 반시계 방향
    elif cp < 0:
        return -1  # 시계 방향
    else:
        return 0  # 일직선

# def convex_hull(points):
#     """
#     Graham's Scan 알고리즘을 사용하여 Convex Hull을 찾는 함수.

#     :param points: 점들의 리스트 [(x1, y1), (x2, y2), ...]
#     :return: Convex Hull을 이루는 점들의 리스트
#     """
#     # 기준점 선택
#     points = sorted(points)
#     p0 = points[0]

#     # 기준점을 기준으로 반시계 방향으로 정렬
#     points = sorted(points, key=lambda p: (p[1] - p0[1]) / (p[0] - p0[0]) if p[0] != p0[0] else float('inf'))

#     # Convex Hull 구성
#     hull = []
#     for p in points:
#         while len(hull) > 1 and ccw(hull[-2], hull[-1], p) <= 0:
#             hull.pop()
#         hull.append(p)

#     return hull

# # 예시 사용
# points = [(0, 0), (1, 1), (2, 2), (2, 0), (2, 4), (3, 3)]
# hull = convex_hull(points)
# print("Convex Hull:", hull)



'''
2
'''

import math

def polar_angle(p0, p1):
    y_span = p1[1] - p0[1]
    x_span = p1[0] - p0[0]
    return math.atan2(y_span, x_span)

def distance(p0, p1):
    return math.sqrt((p1[0] - p0[0])**2 + (p1[1] - p0[1])**2)

def cross_product(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p1[1] - p0[1]) * (p2[0] - p0[0])

def graham_scan(points):
    # 기준점 선택
    start = min(points, key=lambda p: (p[1], p[0]))
    points.remove(start)

    # 기준점을 기준으로 점들을 반시계 방향으로 정렬
    points.sort(key=lambda p: (polar_angle(start, p), distance(start, p)))

    # 볼록 껍질 구성
    hull = [start, points[0], points[1]]
    for p in points[2:]:
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull

# 예제 점들
points = [(0, 0), (1, 1), (2, 2), (2, 0), (2, 4), (3, 3), (4, 2)]
hull = graham_scan(points)
print("볼록 껍질:", hull)
