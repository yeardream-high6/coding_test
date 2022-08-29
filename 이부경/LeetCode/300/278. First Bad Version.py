# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        last = n
        while start < last:
            mid = (start + last) // 2
            if isBadVersion(mid):
                last = mid
            else:
                start = mid + 1
        return start
