from typing import Optional, List
from collections import deque
import time
import math

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
            
            val = next(it) # left node
            if val != None:
                parent.left = TreeNode(val)
                dq.append(parent.left)
                
            val = next(it) # right node
            if val != None:
                parent.right = TreeNode(val)
                dq.append(parent.right)
    except StopIteration:
        return root

def tree_to_list(root: Optional[TreeNode]):
    values = []
    if not root:
        return values
    
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

    while len(values) > 0 and values[-1] == None:
        values.pop()
    
    return values

def find_tree(root: Optional[TreeNode], val: Optional[int]) -> 'TreeNode':
    if not root:
        return None
    
    if root.val == val:
        return root
    
    found = find_tree(root.left, val)
    if found:
        return found
    
    found = find_tree(root.right, val)
    if found:
        return found

def stop_watch(func):
    def wrapper(*arg, **kwarg):
        start = time.time()
        ret_val = func(*arg, **kwarg)
        end = time.time()
        print('소요 시간(초): ', round(end - start, 4))
        return ret_val
    return wrapper
