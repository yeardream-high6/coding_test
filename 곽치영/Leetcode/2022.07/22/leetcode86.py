from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_linked_list(it):
    prehead = ListNode(None)
    node = prehead
    for val in it:
        node.next = ListNode(val)
        node = node.next
    return prehead.next

def get_values(head: Optional[ListNode]):
    node = head
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values

class Solution:
    def partition(self, head:Optional[ListNode], x:int) -> Optional[ListNode]:
        lesser_prehead = ListNode(None)
        greater_prehead = ListNode(None)
        lesser_pos = lesser_prehead
        greater_pos = greater_prehead
        pos = head
        while pos:
            if pos.val < x:
                lesser_pos.next = pos
                lesser_pos = pos
            else:
                greater_pos.next = pos
                greater_pos = pos
            pos = pos.next
        lesser_pos.next = greater_prehead.next
        greater_pos.next = None
        return lesser_prehead.next

sol = Solution()

lst = make_linked_list([1,4,3,2,5,2])
lst = sol.partition(lst, 3)
print(get_values(lst))

lst = make_linked_list([7,4,3,2,5,2])
lst = sol.partition(lst, 3)
print(get_values(lst))

lst = make_linked_list([7,4,3,2,5,9])
lst = sol.partition(lst, 3)
print(get_values(lst))

lst = make_linked_list([7,4,3,6,5,9])
lst = sol.partition(lst, 3)
print(get_values(lst))

lst = make_linked_list([1,1,2,2,1,2])
lst = sol.partition(lst, 3)
print(get_values(lst))