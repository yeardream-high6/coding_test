from helper import *

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def f(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p == q:
                return True            
            if not p or not q: # 둘 중 하나라도 None이면 False
                return False
            
            if p.val != q.val:
                return False            
            if not f(p.left, q.right):
                return False
            if not f(p.right, q.left):
                return False
            
            return True
            
        return f(root.left, root.right)

# 100 Same tree 응용
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetricTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p and q:
                return p.val == q.val and isSymmetricTree(p.left, q.right) and isSymmetricTree(p.right, q.left)
            return p is q
        return isSymmetricTree(root.left, root.right)