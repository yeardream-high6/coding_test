class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        h = head
        while h:
            nexthead = h.next
            h.next = prev
            prev = h
            h = nexthead
        return prev
