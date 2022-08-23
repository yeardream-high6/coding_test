from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mat = []
        for m in matrix:
            mat += m
        return sorted(mat)[k-1]

a = Solution().kthSmallest([[1,2],[3,3]], 2)
print(a)