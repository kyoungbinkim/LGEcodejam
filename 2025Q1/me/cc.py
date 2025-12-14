def solve_optimized():
    def find_hole(K, vA, vB, vC, vD):
        if K == 1:
            if [vA, vB, vC, vD] == [1, 0, 0, 0]:
                return (1, 1)
            elif [vA, vB, vC, vD] == [0, 1, 0, 0]:
                return (1, 0)
            elif [vA, vB, vC, vD] == [0, 0, 1, 0]:
                return (0, 1)
            elif [vA, vB, vC, vD] == [0, 0, 0, 1]:
                return (0, 0)
            else:
                return None
        
        # 중앙 타일 결정
        for tile in range(4):
            counts = [vA, vB, vC, vD]
            counts[tile] -= 1
            
            if counts[tile] < 0:
                continue
            
            # 각 사분면에 필요한 타일 개수
            quad_total = (4 ** (K-1) - 1) // 3
            
            # 구멍이 있는 사분면에서 재귀
            sub_result = find_hole(K-1, *counts)  # 간단화
            
            if sub_result:
                half = 2 ** (K-1)
                # 사분면 위치 조정
                if tile == 0:  # 좌상에 구멍
                    return sub_result
                elif tile == 1:  # 우상에 구멍
                    return (sub_result[0], sub_result[1] + half)
                elif tile == 2:  # 좌하에 구멍
                    return (sub_result[0] + half, sub_result[1])
                else:  # 우하에 구멍
                    return (sub_result[0] + half, sub_result[1] + half)
        
        return None
    
    T = int(input())
    for _ in range(T):
        K, vA, vB, vC, vD = map(int, input().split())
        result = find_hole(K, vA, vB, vC, vD)
        if result:
            print(result[0], result[1])
        else:
            print(-1, -1)

solve_optimized()
