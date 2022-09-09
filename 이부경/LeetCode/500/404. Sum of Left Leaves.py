from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        def f(root):
            nonlocal total
            
            if root is None:
                return
            
            left = root.left
            if left and left.left is None and left.right is None:
                total += left.val
            
            f(root.left)
            f(root.right)
        
        f(root)
        return total