from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def visit(i, j):
            if 0 <= i < m and 0 <= j < n:
                if grid[i][j] != '1':
                    return
                
                grid[i][j] = '2'
                visit(i - 1, j)
                visit(i + 1, j)
                visit(i, j - 1)
                visit(i, j + 1)
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    visit(i, j)
                    cnt += 1
                    
        return cnt
                