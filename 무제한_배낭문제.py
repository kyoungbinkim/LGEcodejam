
'''
무제한 배낭문제
갯수 제한이 없는 배낭 문제
'''
def unbounded_knapsack(weights, values, max_weight):
    """
    무제한 배낭 문제를 동적 계획법으로 해결하는 함수.

    :param weights: 물건들의 무게 리스트
    :param values: 물건들의 가치 리스트
    :param max_weight: 배낭의 최대 무게 제한
    :return: 최대 가치
    """
    n = len(weights)
    # DP 테이블 초기화
    dp = [0] * (max_weight + 1)

    # DP 테이블 채우기
    for w in range(max_weight + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[max_weight]