# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs_count(root, k):
            if not root:
                return 0
            left = dfs_count(root.left, k)
            if left == -1:
                return -1
            if k == left + 1:
                nonlocal ans
                ans = root.val
                return -1
            right = dfs_count(root.right, k - left - 1)
            if right == -1:
                return -1
            return left + right + 1
        
        dfs_count(root,k)
        return ans

        