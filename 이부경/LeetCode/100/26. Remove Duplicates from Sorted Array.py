from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = nums[0]
        
        i = 1
        while i < len(nums):
            if current >= nums[i]:
                del nums[i]
            else:
                current = nums[i]
                i += 1

        return len(nums)
    
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
a = Solution().removeDuplicates([1,1,2])
print(a)

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
a = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(a)