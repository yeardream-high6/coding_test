from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums:
            start_index = bisect_left(nums, target)
            if start_index < len(nums) and nums[start_index] == target:
                last_index = bisect_right(nums, target) - 1
                return [start_index, last_index]
        return [-1, -1]
        
a = Solution().searchRange(nums = [2,2], target = 3)
print(a)