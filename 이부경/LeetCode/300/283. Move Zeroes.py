from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        cnt = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                cnt += 1
            else:
                i += 1
        nums.extend([0] * cnt)


# 타인 코드
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k] = nums[i]
                k+=1
        nums[k:] = [0]*(len(nums)-k)