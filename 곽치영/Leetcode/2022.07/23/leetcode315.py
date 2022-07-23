from typing import List

# Ideas from https://grantjenks.com/docs/sortedcontainers/sortedlist.html

from bisect import bisect_left
from itertools import islice

class SortedList:
    def __init__(self, *, factor=1000):
        self.factor = factor
        self.lists = []
        self.maxes = []
    
    def insort_left(self, x) -> int:
        """
        Inserts x at the leftmost position that maintains the sort order.
        Return: inserted position (the number of elements smaller than x)
        """
        lists = self.lists
        maxes = self.maxes

        if not lists:
            lists.append([x])
            maxes.append(x)
            return 0
        
        pos = bisect_left(maxes, x)
        if pos == len(maxes):
            pos -= 1
        
        count = sum(len(list_) for list_ in islice(lists, pos))

        list_pos = lists[pos]
        idx = bisect_left(list_pos, x)

        list_pos.insert(idx, x)
        maxes[pos] = list_pos[-1]
        self._expand(pos, list_pos)

        return count + idx

    def _expand(self, pos, list_pos):
        factor = self.factor
        if len(list_pos) <= factor:
            return

        half = factor // 2
        new_list = list_pos[half:]
        del list_pos[half:]

        self.lists.insert(pos + 1, new_list)
        self.maxes.insert(pos, list_pos[-1])


class Solution:
    def __init__(self, factor=1000):
        self.factor = factor

    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = SortedList(factor=self.factor)
        ans = []
        for num in reversed(nums):
            ans.append(sorted_list.insort_left(num))
            print(num, list(zip(sorted_list.lists, sorted_list.maxes)))
        ans.reverse()
        return ans



import random

sol = Solution(4)

# random.seed(42)
# lst = random.choices(range(4), k=12)
# print(lst)
# print(sol.countSmaller(lst))

# random.seed(42)
# lst = random.choices(range(10), k=30)
# print(lst)
# print(sol.countSmaller(lst))