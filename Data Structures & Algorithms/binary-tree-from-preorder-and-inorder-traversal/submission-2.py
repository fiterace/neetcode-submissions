# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        pos = {v: i for i, v in enumerate(inorder)}
        it = iter(preorder)

        def build(l, r):
            if l > r:
                return None
            val = next(it)
            root = TreeNode(val)
            m = pos[val]
            root.left = build(l, m - 1)    # must run before right
            root.right = build(m + 1, r)
            return root

        return build(0, len(inorder) - 1)
