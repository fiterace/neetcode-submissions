# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Later try KMP with this one
        def isSame(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val if isSame(a.left,b.left) and isSame(a.right, b.right) else False
        
        if not root:
            return False
        
        return True if isSame(root, subRoot) else self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        