class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        
        def traversal(root):
            if root is None:
                return
            ans.append(root.val)
            traversal(root.left)
            traversal(root.right)
        
        traversal(root)
        
        return ans
