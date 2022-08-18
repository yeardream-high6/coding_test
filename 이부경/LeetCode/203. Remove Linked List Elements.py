from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prehead = ListNode(None, head)
        h = prehead
        
        while h.next:
            if h.next.val == val:
                h.next = h.next.next
            else:
                h = h.next
                
        return prehead.next