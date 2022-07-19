class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1_000_000_007
        row = [0] * (k+1)
        row[0] = 1
        for i in range(2, n+1):
            prev_row = row
            row = [1]
            item = 1
            for j in range(1, k+1):
                item = (
                    item
                    + prev_row[j]
                    - (prev_row[l] if (l := j - i) >= 0 else 0)
                ) % MOD
                row.append(item)
        
        return row[k]