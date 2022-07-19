from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for node in lists:
            while(True):
                if node:
                    nums.append(node.val)
                    node = node.next
                if not node:
                    break

        prev_node = None
        node = None
        for n in sorted(nums, reverse=True):
            node = ListNode(n)
            if prev_node:
                node.next = prev_node
            prev_node = node
        return node
    
print(Solution().mergeKLists([None]))
print(Solution().mergeKLists([]))