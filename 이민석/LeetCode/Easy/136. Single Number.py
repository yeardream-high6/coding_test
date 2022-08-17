class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        while len(nums)>1:
            if nums[0]==nums[1]:
               del nums[:2]
            else:
                return nums[0]
        return nums[0]
