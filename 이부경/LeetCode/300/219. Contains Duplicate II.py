from typing import *

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums = [None] + nums
        counter = Counter(nums[:k + 1])
        if counter.most_common()[0][1] > 1:
                return True
        
        prev = None
        for i in range(k + 1, len(nums)):
            counter[nums[i - k - 1]] -= 1
            counter[nums[i]] += 1
            prev = nums[i]
            if counter[nums[i]] > 1:
                return True
            
        return False