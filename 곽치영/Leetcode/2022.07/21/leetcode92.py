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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prehead = ListNode(None, head)

        start = prehead
        for i in range(1, left):
            start = start.next

        reversing = []
        pos = start
        for j in range(left, right+1):
            pos = pos.next
            reversing.append(pos)
        end = pos.next

        pos = start
        for node in reversed(reversing):
            pos.next = node
            pos = node
        pos.next = end

        return prehead.next

sol = Solution()

lst = make_linked_list([1,2,3,4,5,6,7])
lst = sol.reverseBetween(lst, 3, 5)
print(get_values(lst))

lst = make_linked_list([1,2,3,4,5,6,7])
lst = sol.reverseBetween(lst, 1, 3)
print(get_values(lst))

lst = make_linked_list([1,2,3,4,5,6,7])
lst = sol.reverseBetween(lst, 6, 7)
print(get_values(lst))

lst = make_linked_list([1,2,3,4,5,6,7])
lst = sol.reverseBetween(lst, 1, 1)
print(get_values(lst))

lst = make_linked_list([1,2,3,4,5,6,7])
lst = sol.reverseBetween(lst, 7, 7)
print(get_values(lst))

lst = make_linked_list([1,2,3,4,5,6,7])
lst = sol.reverseBetween(lst, 5, 5)
print(get_values(lst))