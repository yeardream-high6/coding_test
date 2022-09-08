from typing import *

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        if len(c1) > len(c2):
            c1, c2 = c2, c1
        
        output = []
        for c in c1.keys():
            if c in c2:
                output += [c] * min(c1[c], c2[c])
        
        return output