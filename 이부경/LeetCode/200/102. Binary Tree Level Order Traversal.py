from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        value_level_list = []
        
        dq = deque()
        def bfs(root):
            if root:
                dq.append((root, 0))
            while(dq):
                node, level = dq.popleft()
                value_level_list.append((node.val, level))
                if node.left:
                    dq.append((node.left, level + 1))
                if node.right:
                    dq.append((node.right, level + 1))

        bfs(root)
        
        answer = []
        val_list = []
        prev_level = 0
        for val, level in value_level_list:
            if prev_level != level:
                answer.append(val_list)
                val_list = []
            val_list.append(val)
            prev_level = level
        if val_list:
            answer.append(val_list)
        return answer

# 타인 코드
class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        
        queue = deque([root])
        
        while queue:
            level = []
            queue_len = len(queue)
            for _ in range(queue_len):
                current = queue.popleft()
                if current:
                    level.append(current.val)
                    
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
            
            if level:
                output.append(level)
        
        return output


null = None
# root = [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

answer= Solution().levelOrder(root)
print(answer)