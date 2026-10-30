# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = float('-inf')

    def maxLineSum(self, root) -> int:
        if not root:
            return 0
        left = max(self.maxLineSum(root.left), 0)
        right = max(self.maxLineSum(root.right), 0)
        temp_ans = left + right + root.val
        self.ans = max(self.ans, temp_ans)
        return max(left, right) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxLineSum(root)
        return int(self.ans)
        