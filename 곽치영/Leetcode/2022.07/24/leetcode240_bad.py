from typing import List

# 분할정복으로 푼 풀이. O(n^1.4)이라서 느립니다.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(i_min, i_max, j_min, j_max):
            nonlocal matrix, target

            print(i_min, i_max, j_min, j_max)

            if i_min > i_max or j_min > j_max:
                return False
            
            i_mid = (i_min + i_max) >> 1
            j_mid = (j_min + j_max) >> 1

            val = matrix[i_mid][j_mid]
            if val < target:
                return (
                    search(i_mid+1, i_max, j_min, j_max)
                    or search(i_min, i_mid, j_mid+1, j_max)
                )
            if val > target:
                return (
                    search(i_min, i_mid-1, j_min, j_max)
                    or search(i_mid, i_max, j_min, j_mid-1)
                )
            return True

        n = len(matrix)
        m = len(matrix[0])
        return search(0,n-1,0,m-1)

sol = Solution()
sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)