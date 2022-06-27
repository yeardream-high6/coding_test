def solution(m, n, puddles):
    MOD = 1000_000_007
    dp = [[1] * n for _ in range(m)]
    for i, j in puddles:
        dp[i-1][j-1] = 0
    
    # dp[0][0] = dp[0][0]
    for j in range(1, n):
        if dp[0][j]:
            dp[0][j] = dp[0][j-1] % MOD
    for i in range(1, m):
        if dp[i][0]:
            dp[i][0] = dp[i-1][0] % MOD
        for j in range(1, n):
            if dp[i][j]:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
    return dp[m-1][n-1] % MOD
