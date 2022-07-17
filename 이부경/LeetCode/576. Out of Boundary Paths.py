from functools import cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 10 ** 9 + 7
        
        @cache
        def f(maxMove, i, j):
            ball_out = 0
            # up
            if i == 0 and maxMove >= 1:
                ball_out += 1
            elif maxMove > 1:
                ball_out += f(maxMove - 1, i - 1, j)
            ball_out %= M
            
            # down
            if i == m - 1 and maxMove >= 1:
                ball_out += 1
            elif maxMove > 1:
                ball_out += f(maxMove - 1, i + 1, j)
            ball_out %= M
            
            # left
            if  j == 0 and maxMove >= 1:
                ball_out += 1
            elif maxMove > 1:
                ball_out += f(maxMove - 1, i, j - 1)
            ball_out %= M
                
            # right
            if  j == n - 1 and maxMove >= 1:
                ball_out += 1
            elif maxMove > 1:
                ball_out += f(maxMove - 1, i, j + 1)
            ball_out %= M

            return ball_out
        
        answer = f(maxMove, startRow, startColumn)
        return answer
        
        
answer = Solution().findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0)
print(answer)
answer = Solution().findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1)
print(answer)