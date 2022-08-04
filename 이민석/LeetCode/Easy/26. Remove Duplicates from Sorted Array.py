class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                l.append(i) 
        for j in sorted(l, reverse=True):
            del nums[j]
        return len(nums)
