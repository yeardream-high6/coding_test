from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        ans = [row]
        for i in range(1, numRows):
            prev_row = row
            row = [1]
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])
            row.append(1)
            ans.append(row)
        return ans