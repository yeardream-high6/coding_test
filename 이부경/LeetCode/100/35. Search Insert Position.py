from typing import List
from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)

a = Solution().searchInsert(nums = [1,3,5,6], target = 7)
print(a)