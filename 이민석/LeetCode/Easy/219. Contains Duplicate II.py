class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums)==len(set(nums)):
            return False
        
        for i in range(len(nums)):
            end = i+k+1
            
            if end > len(nums):
                end = len(nums)
                
            if len(nums[i:end]) != len(set(nums[i:end])):
                return True
                
            else:
                continue
                if i >= len(nums)-k:
                    return False
