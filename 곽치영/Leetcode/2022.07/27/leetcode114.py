from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _flatten(self, root: TreeNode) -> TreeNode:
        
        # print(f"flatting start: {root.val}")
        
        rear = root
        left_subtree = root.left
        right_subtree = root.right
        if left_subtree:
            root.left = None
            root.right = left_subtree
            rear = self._flatten(left_subtree)
        if right_subtree:
            rear.right = right_subtree
            rear = self._flatten(right_subtree)
            
        # print(f"flatted: {root.val} to {rear.val}")
        
        return rear
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root:
            self._flatten(root)
