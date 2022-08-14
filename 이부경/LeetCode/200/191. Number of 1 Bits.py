class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            n -= n & -n
            cnt += 1
        return cnt