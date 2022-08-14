from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def f(root: Optional[TreeNode], depth):
            nonlocal max_depth
            if root:
                if max_depth < depth:
                    max_depth = depth
                f(root.left, depth + 1)
                f(root.right, depth + 1)
        f(root, 1)
        return max_depth

# 타인 코드    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            right = recur(root.right)
            return max(left,right) + 1
        return recur(root)