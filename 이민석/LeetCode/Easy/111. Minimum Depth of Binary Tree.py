# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        cnt = 1
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        elif not root.left:
            cnt += self.minDepth(root.right)
        elif not root.right:
            cnt += self.minDepth(root.left)
        else:
            l_depth = self.minDepth(root.left)
            r_depth = self.minDepth(root.right)
            cnt += min(l_depth,r_depth)
        
        return cnt
