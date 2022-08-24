from typing import List

class BinaryIndexedTree():
    def __init__(self, values):
        self.arr = [0] * len(values) + [0]
        self.values = values.copy()
        for i, v in enumerate(values):
            self.add(i, v)
    
    def add(self, index, val):
        i = index + 1 # 0을 사용하지 않음
        while i < len(self.arr):
            self.arr[i] += val
            i += (i & -i)
    
    def sum(self, index):
        total = 0
        i = index + 1 # 0을 사용하지 않음
        while i > 0:
            total += self.arr[i]
            i -= (i & -i)
        return total
    
    def update(self, i, val):
        self.add(i, val - self.values[i])
        self.values[i] = val
    
    def sum_range(self, start, last):
        a = self.sum(last)
        b = self.sum(start - 1) if start > 0 else 0
        c = a - b
        return c
    
class NumArray:
    def __init__(self, nums: List[int]):
        self.bit =  BinaryIndexedTree(nums)

    def update(self, index: int, val: int) -> None:
        self.bit.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.sum_range(left, right)
        
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


# 타인 코드
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums=nums
        self.summ=sum(self.nums)
        
    def update(self, index: int, val: int) -> None:
        tm=self.nums[index]
        self.nums[index]=val
        self.summ=self.summ-tm+val
        
    def sumRange(self, left: int, right: int) -> int:
        lefts=sum(self.nums[:left])
        rights=sum(self.nums[right+1:])
        return self.summ-lefts-rights