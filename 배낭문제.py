'''
베낭문제 1개만 선택하는 배낭문제...
'''

def knapsack(weights, values, max_weight):
    """
    0/1 배낭 문제를 동적 계획법으로 해결하는 함수.

    :param weights: 물건들의 무게 리스트
    :param values: 물건들의 가치 리스트
    :param max_weight: 배낭의 최대 무게 제한
    :return: 최대 가치
    """
    n = len(weights)
    # DP 테이블 초기화
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    # DP 테이블 채우기
    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][max_weight]