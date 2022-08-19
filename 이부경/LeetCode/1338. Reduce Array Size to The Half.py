from typing import *
from bisect import bisect_left
from itertools import accumulate

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n_removed = 0
        for i, n in enumerate(Counter(arr).most_common(), 1):
            n_removed += n[1]
            if n_removed * 2 >= len(arr):
                return i
    
# 치영
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        return bisect_left(list(accumulate(sorted(Counter(arr).values(), reverse=True))), len(arr) // 2) + 1

#a = Solution().minSetSize([7,7,7,7,7,7])
a = Solution().minSetSize([3,3,3,3,5,5,5,2,2,7])
print(a)