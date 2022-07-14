from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# preorder, inorder를 앞에서부터 읽으면서 처리하기 위해 도와주는 클래스.
# 가장 최근 값을 조회하는 curr와, 다음 값으로 넘어가는 next()를 구현합니다.
# 끝에 다다르면 None을 반환합니다.
class Pointer:
    def __init__(self, iter):
        self.iter = iter
        self.curr = None
        self.next()
    def next(self):
        try:
            self.curr = next(self.iter)
        except StopIteration:
            self.curr = None
        return self.curr

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_check = set([None])

        p_pre = Pointer(iter(preorder))
        p_in = Pointer(iter(inorder))

        def dfs():
            # 디버그 용
            # print(p_in.curr, p_pre.curr)

            # preorder 첫번째 값이 부모입니다.
            node = TreeNode(p_pre.curr)

            # preorder 첫 값과 inorder 첫 값이 같다면 왼쪽 자식이 없습니다.
            if p_pre.curr == p_in.curr:
                # preorder, inorder 둘 다 다음으로 넘어갑니다.
                preorder_check.add(p_pre.curr)
                p_pre.next()
                p_in.next()

                # inorder 첫 값이 이미 방문한 값이면 부모로 올라갑니다.
                if p_in.curr in preorder_check:
                    return node

                # inorder 첫 값이 처음 보는 값이면 오른쪽 자식입니다.
                node.right = dfs()
                return node

            # preorder 첫 값과 inorder 첫 값이 다르므로 왼쪽 자식이 있습니다.

            # preorder만 다음으로 넘깁니다.
            preorder_check.add(p_pre.curr)
            p_pre.next()
            
            # 왼쪽 자식을 구합니다.
            node.left = dfs()
            p_in.next()

            # inorder 첫 값이 이미 방문한 값이면 부모로 올라갑니다.
            if p_in.curr in preorder_check:
                return node
            
            # inorder 첫 값이 처음 보는 값이면 오른쪽 자식입니다.
            node.right = dfs()
            return node

        tree = dfs()
        return tree

def preorder(node):
    result = [node.val]
    if node.left:
        result += preorder(node.left)
    if node.right:
        result += preorder(node.right)
    return result

def inorder(node):
    result = []
    if node.left:
        result += inorder(node.left)
    result += [node.val]
    if node.right:
        result += inorder(node.right)
    return result

tree = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
print(preorder(tree), inorder(tree))

tree = Solution().buildTree([1, 2, 3, 4, 5, 6, 7], [1, 5, 4, 3, 7, 6, 2])
print(preorder(tree), inorder(tree))