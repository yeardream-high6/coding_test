from typing import List

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while(len(nums) > 1):
            newNums = []
            for i in range(len(nums) // 2):
                if i % 2:
                    value = max(nums[2 * i], nums[2 * i + 1])
                else:
                    value = min(nums[2 * i], nums[2 * i + 1])
                newNums.append(value)
            nums = newNums
            
        return nums[0]

input_list = [[1,3,5,2,4,8,2,2],
            [3]
            ]
for i in input_list:
    answer = Solution().minMaxGame(i)
    print(answer)