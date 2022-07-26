from typing import Optional, List
from collections import deque

null = None

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

def linked_list_to_list(head: Optional[ListNode]):
    node = head
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_tree(value_list: 'List') -> 'TreeNode':
    if not value_list:
        return None
    
    it = iter(value_list)
    try:
        dq = deque()
        root = TreeNode(next(it))
        dq.append(root)
        while True:
            parent = dq.popleft()
            parent.left = TreeNode(next(it))
            dq.append(parent.left)
            parent.right = TreeNode(next(it))
            dq.append(parent.right)
    except StopIteration:
        return root

def tree_to_list(root: Optional[TreeNode]):
    values = []
    dq = deque()
    dq.append(root)
    values.append(root.val)
    while dq:
        parent = dq.popleft()
        if parent.left:
            values.append(parent.left.val)
            dq.append(parent.left)
        else:
            values.append(None)
        if parent.right:
            values.append(parent.right.val)
            dq.append(parent.right)
        else:
            values.append(None)

    while not values[-1]:
        values.pop()
    
    return values