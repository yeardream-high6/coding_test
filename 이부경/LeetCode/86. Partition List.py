from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = ListNode(None)
        right_head = ListNode(None)
        
        lh = left_head
        rh = right_head
        
        h = head
        while(h):
            next_node = h.next
            if h.val < x:
                lh.next = h
                lh = h
            else:
                rh.next = h
                rh = h
            
            h = next_node
        lh.next = right_head.next
        rh.next = None
        return left_head.next


head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
h = Solution().partition(head, 3)
