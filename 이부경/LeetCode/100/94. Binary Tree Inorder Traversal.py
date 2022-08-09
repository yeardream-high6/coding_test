from typing import Optional, List
from collections import deque

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.output = []
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def f(root: Optional[TreeNode]):
            if not root:
                return 
            f(root.left)
            self.output.append(root.val)
            f(root.right)
        f(root)
        return self.output

# 타인 코드    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = deque()
        node = root
        while node or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res