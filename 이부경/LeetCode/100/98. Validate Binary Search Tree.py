from typing import *
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# 타인 코드
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(root: Optional[TreeNode], lower, upper)-> bool:
            if not root:
                return True
            val = root.val
            return lower < val < upper and isBST(root.left, lower, val) and isBST(root.right, val, upper)
        return isBST(root, -math.inf, +math.inf)
