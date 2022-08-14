from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(p[i-1][j] + p[i-1][j-1])
            p.append(row)
        return p

a = Solution().generate(5)
print(a)