# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        level = deque([root])
        ans = []
        while level:
            new_level = []
            level_ans = []
            while level:
                top = level.popleft()
                level_ans.append(top.val)
                if top.left: new_level.append(top.left)
                if top.right: new_level.append(top.right)
            level = deque(new_level)
            ans.append(level_ans)
        return ans
        