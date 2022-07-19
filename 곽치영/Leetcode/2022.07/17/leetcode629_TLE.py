class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1_000_000_007
        dp = [[0] * (k+1) for _ in range(n+1)]
        dp[1][0] = 1
        for i in range(2, n+1):
            prev_row = dp[i-1]
            row = dp[i]
            for j in range(k+1):
                item = 0
                for l in range(max(0, j-i+1), j+1):
                    item += prev_row[l]
                row[j] = item % MOD
        
        return dp[n][k]