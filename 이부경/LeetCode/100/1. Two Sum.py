from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        # 해시를 사용하는 방법으로 다시 풀음. O(n)
        for i, n in enumerate(nums):
            if target - n in num_dict:
                return [num_dict[target - n], i]
            num_dict[n] = i
            
a = Solution().twoSum(nums = [2,7,11,15], target = 9)
print(a)