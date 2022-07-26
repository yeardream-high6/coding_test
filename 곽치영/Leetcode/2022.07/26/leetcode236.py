# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ### dfs 순회하면서 p와 q 사이에 나타나는 노드 중 가장 깊이가 얕은 노드가 최소공통조상입니다.
        # p, q가 여러번 나타날 수 있지만 아무거나 선택해도 같습니다. (두 p 사이의 깊이는 p보다 깊다)
        # Example 1 dfs: 3 5 6 5 2 7 2 4 2 5 3 1 0 1 8 1 3
        #              :   p   p               q   q
        # depth        : 1 2 3 2 3 4 3 4 3 2 1 2 3 2 3 2 1

        targets = [p, q]

        flag = False
        min_depth = None
        min_node = None

        def update(node, depth):
            nonlocal targets
            nonlocal flag, min_depth, min_node

            target_i = next((i for i, t in enumerate(targets) if node is t), None)
            if target_i is not None:
                targets.pop(target_i)
            is_target = target_i is not None
            
            if flag:
                if min_depth > depth:
                    min_depth = depth
                    min_node = node
            elif is_target:
                flag = True
                min_depth = depth
                min_node = node
            
            if not targets:
                return min_node
            return None

        ### dfs 순회를 재귀 없이 구현

        back = object()
        path_stack = [TreeNode(None)]
        cmd_stack = [root]

        while cmd_stack:
            cmd = cmd_stack.pop()

            # go down
            if cmd is not back:
                prev = path_stack[-1]
                curr = cmd
                path_stack.append(curr)
                cmd_stack.append(back)
                if curr.right:
                    cmd_stack.append(curr.right)
                if curr.left:
                    cmd_stack.append(curr.left)

                # print(f"go down {prev.val} {curr.val}")
                curr_depth = len(path_stack) - 1
                if result := update(curr, curr_depth): return result

            # go up
            else:
                prev = path_stack.pop()
                curr = path_stack[-1]

                # print(f"go up {prev.val} {curr.val}")
                curr_depth = len(path_stack) - 1
                if result := update(curr, curr_depth): return result
