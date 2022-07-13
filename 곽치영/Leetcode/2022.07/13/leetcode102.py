from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        flag = object()
        dq = deque([flag, root])
        answer = []

        while True:
            node = dq.popleft()
            if node is flag:
                if not dq:
                    break
                answer.append([])
                dq.append(flag)
                continue

            answer[-1].append(node.val)
            if node.left is not None:
                dq.append(node.left)
            if node.right is not None:
                dq.append(node.right)

        return answer

sol = Solution()

print(
    sol.levelOrder(
        TreeNode(
            3,
            TreeNode(9),
            TreeNode(
                20,
                TreeNode(15),
                TreeNode(7),
            ),
        )
    )
)

print(sol.levelOrder(TreeNode(1)))

print(sol.levelOrder(None))