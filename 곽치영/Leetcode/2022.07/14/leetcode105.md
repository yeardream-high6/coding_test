## 다른사람 풀이
- [Simple O(n) without map](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34543/Simple-O(n)-without-map)
```python
def buildTree(self, preorder, inorder):
    def build(stop):
        if inorder and inorder[-1] != stop:
            root = TreeNode(preorder.pop())
            root.left = build(root.val)
            inorder.pop()
            root.right = build(stop)
            return root
    preorder.reverse()
    inorder.reverse()
    return build(None)
```
정말 간결하네요.