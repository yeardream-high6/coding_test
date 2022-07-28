from helper import *

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode(None)
        dummyHead = merged_list
        node1 = list1
        node2 = list2
        while node1 and node2:
            if node1.val < node2.val:
                merged_list.next = node1
                node1 = node1.next
            else:
                merged_list.next = node2
                node2 = node2.next
            merged_list = merged_list.next
        
        # 나머지 노드 이어 붙이기
        if node1:
            merged_list.next = node1
        if node2:
            merged_list.next = node2
        
        return dummyHead.next
    
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]    
# Input: list1 = [], list2 = []
# Output: []
# Input: list1 = [], list2 = [0]
# Output: [0]
list1 = make_linked_list([1,2,4])
list2 = make_linked_list([1,3,4])
a = Solution().mergeTwoLists(list1, list2)
a = linked_list_to_list(a)
print(a)