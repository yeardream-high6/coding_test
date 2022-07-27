# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from helper import *

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        dq = deque()
        # 트리의 모든 노드를 전위 순회 순서로 큐에 넣습니다.
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            dq.append(root)
            dfs(root.left)
            dfs(root.right)                
        dfs(root)
        
        # FIFO 순서로 꺼내어 right에 자식 노드를 달아줍니다.
        parent = None
        while dq:
            me = dq.popleft()
            #print(me.val)
            me.left = None
            me.right = None
            if parent:
                parent.right = me
            parent = me


#Input: root = [1,2,5,3,4,null,6]
#Output: [1,null,2,null,3,null,4,null,5,null,6]
# root = make_tree([1,2,5,3,4,null,6])
# Solution().flatten(root)
# print(tree_to_list(root))

root = make_tree([])
Solution().flatten(root)
print(tree_to_list(root))

# root = make_tree([0])
# Solution().flatten(root)
# print(tree_to_list(root))