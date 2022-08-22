from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        
        h = head
        while h:
            nums.append(h.val)
            h = h.next
            
        for i in range(len(nums) // 2):
            if nums[i] != nums[- i - 1]:
                return False

        return True