# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root) -> int:
        best = root.val

        def dfs(node):
            nonlocal best
            l = r = 0
            if node.left:
                l = dfs(node.left)
                if l < 0: l = 0
            if node.right:
                r = dfs(node.right)
                if r < 0: r = 0
            v = node.val
            s = l + r + v
            if s > best: best = s
            return (l if l > r else r) + v

        dfs(root)
        return best
        