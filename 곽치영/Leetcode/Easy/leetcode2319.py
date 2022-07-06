from typing import List

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if (j == i or j == n - i - 1) ^ (item != 0):
                    return False
        return True

Solution().checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]])