# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root) -> int:

        # iterative version: also solved with dfs
        best = root.val
        order, stack = [], [root]
        while stack:
            n = stack.pop()
            order.append(n)
            if n.left: stack.append(n.left)
            if n.right: stack.append(n.right)

        gain = {None: 0}  # best non-negative downward path from each node
        for n in reversed(order):  # children always come before parents
            l, r = gain[n.left], gain[n.right]
            s = l + r + n.val
            if s > best: best = s
            g = (l if l > r else r) + n.val
            gain[n] = g if g > 0 else 0
        return best
        