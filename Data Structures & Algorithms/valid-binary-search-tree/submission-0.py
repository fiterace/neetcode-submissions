# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left = True
        if root.left:
            left = (root.left.val < root.val and self.isValidBST(root.left))
        right = True
        if root.right:
            right = (root.right.val > root.val and self.isValidBST(root.right))
        return right and left

        