from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        self.fenwick = [0] * (len(nums) + 1)
        for i, n in enumerate(nums):
            self.add(i, n)

    def update(self, index: int, val: int) -> None:
        i = index
        self.add(i, val - self.nums[i])
        self.nums[i] = val
        

    def sumRange(self, left: int, right: int) -> int:
        a = self.sum(right)
        b = self.sum(left - 1) if left > 0 else 0
        c = a - b
        return c
        
    def add(self, index: int, val: int) -> None:
        i = index + 1 # 0을 사용하지 않으므로
        while i < len(self.fenwick):
            self.fenwick[i] += val
            i = i + (i & -i) # 맨 오른쪽 1을 더하기
        
    def sum(self, index: int) -> None:
        i = index + 1 # 0을 사용하지 않으므로
        total = 0
        while i > 0:
            total += self.fenwick[i]
            i = i & (i - 1) # 맨 오른쪽 1을 0으로
        return total

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
nums = [1, 3, 5]
obj = NumArray(nums)
a = obj.sumRange(0,2)
print(a)
obj.update(1,2)
a = obj.sumRange(0,2)
print(a)