#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from helper import *

class TreeNodeExt(TreeNode):
    def __init__(self, x, parent):
        super().__init__(x.val)
        self.parent = parent
        self.left = x.left
        self.right = x.right
        #self.val = x.val
        
    def get_ancesters(self):
        ancesters = []
        
        me = self
        while me:
            ancesters.append(me)
            me = me.parent
        return ancesters

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_p_q_node():
            p_node = None
            q_node = None
            dq = deque()
            dq.append(TreeNodeExt(root, None))
            while dq:
                parent = dq.popleft()
                if parent.val == p.val:
                    p_node = parent
                if parent.val == q.val:
                    q_node = parent
                
                if p_node and q_node:
                    return p_node, q_node
                
                if parent.left:
                    dq.append(TreeNodeExt(parent.left, parent))
                if parent.right:
                    dq.append(TreeNodeExt(parent.right, parent))
            return p_node, q_node

        p_node, q_node = get_p_q_node()        
        p_parents = p_node.get_ancesters()
        q_parents = q_node.get_ancesters()
        
        
        if len(p_parents) < len(q_parents):
            parents1, parents2 = p_parents, q_parents
        else:
            parents1, parents2 = q_parents, p_parents
        
        for node in parents2:
            if node in parents1:
                return node

# 타인 코드
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = 0
        
        def solve(root,p,q) :
            if not root :
                return False
            
            mid = root == p or root == q
            
            left = solve(root.left,p,q)
            right = solve(root.right,p,q)
            
            if left + right + mid == 2 :
                self.result = root
            
            return left or right or mid
        solve(root,p,q)
        return self.result    

# 타인 코드
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in [None, p, q]:
            return root
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right

p = TreeNode(5)
q = TreeNode(4)
root = make_tree([3,5,1,6,2,0,8,null,null,7,4])
a = Solution().lowestCommonAncestor(root, p, q)
print(a.val)