# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depthOfTree(root):
            if not root:
                return 0
            left = depthOfTree(root.left)
            right = depthOfTree(root.right)
            self.diameter = max(self.diameter,left + right)
            return max(left,right) + 1
        
        depthOfTree(root)
        return self.diameter
        