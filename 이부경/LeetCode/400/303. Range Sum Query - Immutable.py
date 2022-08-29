from typing import *

class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        for i in range(len(nums)):
            self.sums[i] =  nums[i] + (self.sums[i - 1] if i != 0 else 0)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - (self.sums[left - 1] if left > 0 else 0)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)