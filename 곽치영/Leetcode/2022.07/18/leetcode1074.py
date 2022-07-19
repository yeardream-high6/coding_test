from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[[None] * (m+1) for _ in range(m+1)] for _ in range(n+1)]
        for j in range(m+1):
            dp[0][j] = 0
        for i in range(1, n+1):
            dp[i][0] = 0
            for j in range(1, m+1):
                dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

        #   │   │
        # ──┼───┤ l <- count l where (dp[i][j] - dp[i][k]) - (dp[l][j] - dp[l][k]) = target
        #   │   │
        # ──┴───┘ i
        #   k   j

        ans = 0
        for j in range(1, m+1):
            for k in range(j):
                counter = dict()
                for i in range(0, n+1):
                    sumijk = dp[i][j] - dp[i][k]
                    diff = sumijk - target
                    ans += counter.get(diff, 0)
                    counter[sumijk] = counter.get(sumijk, 0) + 1

        return ans

print(Solution().numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0))