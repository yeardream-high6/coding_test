from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        half = len(nums) // 2
        counter = Counter(nums)
        dic = dict(counter)
        for key,value in dic.items():
            if value > half:
                return key
        
