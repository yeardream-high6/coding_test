from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def f(root: Optional[TreeNode], targetSum: int, total: int) -> bool:
            if root is None:
                return False
            
            if root.left == root.right: # 양쪽이 None일 경우 == 말단 노드
                return root.val + total == targetSum
            
            left = f(root.left, targetSum, root.val + total)
            right = f(root.right, targetSum, root.val + total)
            return left or right
        
        return f(root, targetSum, 0)
