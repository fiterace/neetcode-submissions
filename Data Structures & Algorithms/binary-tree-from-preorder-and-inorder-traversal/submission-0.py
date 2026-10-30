# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        inorder_lookup = {inorder[i]: i for i in range(n)}
        preorder_lookup = {preorder[i]: i for i in range(n)}

        def build_tree_recursive(i, j, l, r):
            if l > r or i > j:
                return None
            nonlocal inorder, preorder, inorder_lookup, preorder_lookup
            root_val = preorder[i]
            root = TreeNode(root_val)
            m = inorder_lookup[root_val]
            k = m - l + i # left_size + i
            root.left = build_tree_recursive(i + 1, k, l, m - 1)
            root.right = build_tree_recursive(k + 1, j, m + 1, r)
            return root

        return build_tree_recursive(0, n - 1, 0, n - 1)
