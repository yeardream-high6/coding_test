from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        
        for i in range(1, target + 1):
            for n in nums:
                if i - n >= 0: #  dp[i-n]은 이전 값
                    dp[i] += dp[i-n]
            
        return dp[target]


# a = Solution().combinationSum4(nums = [9], target = 3)
# print(a)

# nums = [4,2,1]
# target = 32
# a = Solution().combinationSum4(nums, target)
# print(a)