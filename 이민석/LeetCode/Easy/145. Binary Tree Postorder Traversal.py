class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        
        def traversal(root):
            if root is None:
                return
            
            traversal(root.left)
            traversal(root.right)
            ans.append(root.val)
        
        traversal(root)
        
        return ans
