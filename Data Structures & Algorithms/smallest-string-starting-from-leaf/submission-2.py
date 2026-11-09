# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None
        run = []
        def dfs(root):
            run.append(chr(ord('a') + root.val))
            if not root.left and not root.right:
                nonlocal ans
                cur = "".join(reversed(run))
                if ans is None or cur < ans:
                    ans = cur
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            run.pop()
        dfs(root)
        return ans



        