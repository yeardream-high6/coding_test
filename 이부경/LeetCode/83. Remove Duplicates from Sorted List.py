from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = head
        h = head
        prev = ListNode(None)
        while h:
            if h.val == prev.val:
                prev.next = h.next
            else:
                prev = h
            h = h.next
        return output

# 타인 코드
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp:
            while temp.next and temp.next.val == temp.val:
                temp.next = temp.next.next     # skip duplicated node
            temp = temp.next     # not duplicate of current node, move to next node
        return head    