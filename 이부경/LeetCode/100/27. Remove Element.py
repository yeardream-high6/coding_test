from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i = 0
        while i < len(nums):
            current = nums[i]
            if current == val:
                del nums[i]
            else:
                i += 1            
        return len(nums)

a = Solution().removeElement(nums = [3,2,2,3], val = 3)
print(a)

a = Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
print(a)