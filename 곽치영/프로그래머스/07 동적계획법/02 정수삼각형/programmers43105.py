def solution(triangle):
    n = len(triangle)
    dp = [None] * n
    dp[-1] = triangle[-1].copy()
    for i in range(n-2, -1, -1):
        dp[i] = [max(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j] for j in range(i+1)]
    return dp[0][0]
