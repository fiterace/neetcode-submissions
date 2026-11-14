# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def can_form_pal(self, arr):
        num_odds = 0
        cts = defaultdict(int)
        for i in arr:
            cts[i] += 1
        for i, v in cts.items():
            if v%2:
                num_odds += 1
        return num_odds < 2

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        visited = defaultdict(bool)
        st = [root]
        visited[root] = True
        ans = 0
        while st:
            top = st[-1]
            if not top.left and not top.right:
                ans += self.can_form_pal([node.val for node in st])
            if top.left and not visited[top.left]:
                st.append(top.left)
                visited[top.left] = True
            elif top.right and not visited[top.right]:
                st.append(top.right)
                visited[top.right] = True
            else:
                st.pop()
        return ans


        