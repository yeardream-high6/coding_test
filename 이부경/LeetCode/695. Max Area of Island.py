from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = [[0] * n for _ in range(m)]
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if visited[i][j] or not grid[i][j]:
                return 0

            visited[i][j] = 1
            up = dfs(i + 1, j)
            down = dfs(i - 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            return 1 + up + down + left + right

        maximum_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    maximum_area = max(dfs(i, j), maximum_area)
                visited[i][j] = 1
        return maximum_area
        
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
answer = Solution().maxAreaOfIsland(grid)
print(answer)