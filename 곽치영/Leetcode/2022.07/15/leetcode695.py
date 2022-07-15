from typing import List

from collections import deque
from copy import deepcopy

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        grid = deepcopy(grid)
        n = len(grid)
        m = len(grid[0])

        adjs = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        ]
        
        def get_area(i, j):
            # print(i, j)
            grid[i][j] = 0
            area = 1
            for di, dj in adjs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj]:
                        area += get_area(ni, nj)
            return area

        ans = 0

        dq = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    area = get_area(i, j)
                    if ans < area:
                        ans = area
        
        return ans

print(Solution().maxAreaOfIsland(
    [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0],
    ]
))