class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 1_000_000_007
        curr = [[0] * (n+2) for _ in range(m+2)]
        prev = [[None] * (n+2) for _ in range(m+2)]
        for i in range(1, m+1):
            curr[i][0] = 1
            curr[i][n+1] = 1
        for j in range(1, n+1):
            curr[0][j] = 1
            curr[m+1][j] = 1
        for _ in range(maxMove):
            curr, prev = prev, curr
            for i in range(1, m+1):
                for j in range(1, n+1):
                    curr[i][j] = (
                          prev[i-1][j]
                        + prev[i][j-1]
                        + prev[i+1][j]
                        + prev[i][j+1]
                    ) % MOD
            for i in range(1, m+1):
                curr[i][0] = 1
                curr[i][n+1] = 1
            for j in range(1, n+1):
                curr[0][j] = 1
                curr[m+1][j] = 1
        return curr[startRow+1][startColumn+1]