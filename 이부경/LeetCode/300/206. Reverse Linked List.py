from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        prev_node = None
        while h:
            next_node = h.next
            h.next = prev_node
            prev_node = h
            h = next_node
        return prev_node