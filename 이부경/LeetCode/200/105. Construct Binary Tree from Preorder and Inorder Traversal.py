from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node_dict = {}

        prev_index = 0
        index = 0
        for i in range(len(preorder)):
            val =  preorder[i]
            node = TreeNode(val)
            node_dict[val] = node
            index = inorder.index(val)
            
            if i > 0:
                if index < prev_index:
                    node_dict[inorder[prev_index]].left = node
                else:
                    for i in range(index - 1, prev_index - 1, -1):
                        if inorder[i] in node_dict:
                            node_dict[inorder[i]].right = node
                            break
                        
            prev_index  = index
            
        return node_dict[preorder[0]]

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
answer = Solution().buildTree(preorder, inorder)
print(answer)