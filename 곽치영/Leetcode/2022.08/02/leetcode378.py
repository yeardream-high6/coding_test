from typing import List

class Solution:
    def count_le(self, n, m, matrix, value):
        k = 0
        i = 0
        j = m - 1
        while i < n and j >= 0:
            if matrix[i][j] <= value:
                k += j + 1
                i += 1
            else:
                j -= 1
        return k
    
    def count_lt(self, n, m, matrix, value):
        k = 0
        i = 0
        j = m - 1
        while i < n and j >= 0:
            if matrix[i][j] < value:
                k += j + 1
                i += 1
            else:
                j -= 1
        return k
        
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        i = 0
        j = m - 1
        while i < n and j >= 0:
            if self.count_le(n, m, matrix, matrix[i][j]) < k:
                i += 1
            elif self.count_lt(n, m, matrix, matrix[i][j]) >= k:
                j -= 1
            else:
                return matrix[i][j]
