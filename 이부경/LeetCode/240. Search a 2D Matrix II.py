from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])

        i = 0
        j = N - 1
        for _ in range(M + N):      
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target and i + 1 < M:
                i += 1
            elif j - 1 >= 0 :
                j -= 1
            
        return False

# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 5
# a = Solution().searchMatrix(matrix, target)
# print(a)

matrix = [[-1,3]]
target = -1
a = Solution().searchMatrix(matrix, target)
print(a)
