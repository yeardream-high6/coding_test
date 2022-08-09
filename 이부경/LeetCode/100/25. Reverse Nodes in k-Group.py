from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        node_list = [None] * k
        before_head = None
        answer = None
        h = head
        while(True):
            i = 0
            while(h and i < k):
                node_list[i] = h
                h = h.next
                if h:
                    i += 1
                
            if i + 1 < k:
                break
            
            node_list[0].next = node_list[k - 1].next
            for i in reversed(range(1, k)):
                node_list[i].next = node_list[i - 1]
            
            if before_head:
                before_head.next = node_list[k - 1]
            else:
                answer = node_list[k - 1]
            before_head = node_list[0]
        return answer

n = 2
head = ListNode(1)
h = head
for i in range(2, n + 1):
    h.next = ListNode(i)
    h = h.next

h = Solution().reverseKGroup(head, 2)
while(h):
    print(h.val, end=' ')
    h = h.next
print()