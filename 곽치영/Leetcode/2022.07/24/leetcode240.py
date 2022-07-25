from typing import List

# 왼쪽 끝 모서리부터 비교하면 항상 1행 또는 1열을 제외할 수 있습니다. O(n+m)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i, j = n-1, 0
        while i >= 0 and j < m:
            val = matrix[i][j]
            if val < target:
                j += 1
            elif val > target:
                i -= 1
            else:
                return True
        return False
