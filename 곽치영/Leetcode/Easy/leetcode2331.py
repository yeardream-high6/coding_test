from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def _evalTree(root):
            if root.left is None:
                return root.val
            else:
                if root.val == 2:
                    return _evalTree(root.left) or _evalTree(root.right)
                if root.val == 3:
                    return _evalTree(root.left) and _evalTree(root.right)
        return _evalTree(root)
