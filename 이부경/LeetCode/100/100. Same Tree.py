from helper import *

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:         
        def f(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p == q:
                return True            
            if not p or not q: # 둘 중 하나라도 None이면 False
                return False
            
            if p.val != q.val:
                return False            
            if not f(p.left, q.left):
                return False
            if not f(p.right, q.right):
                return False
            
            return True
            
        return f(p, q)

# 타인 코드
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q    