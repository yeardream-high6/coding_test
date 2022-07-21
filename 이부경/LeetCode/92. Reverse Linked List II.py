from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_prev = None 
        left_node = None

        trailer = ListNode(None, head)
        h = trailer
        i = 0
        while(h):
            next_node = h.next
            if i == left - 1:
                left_prev = h
            if i == left:
                left_node = h
            if left < i and i <= right:
                h.next = prev
            if i == right:
                left_node.next = next_node
                left_prev.next = h
            prev = h
            h = next_node
            
            i += 1
        return trailer.next

root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
h = Solution().reverseBetween(root, 2, 4)
while(h):
    print(h.val, end=" ")
    h = h.next
