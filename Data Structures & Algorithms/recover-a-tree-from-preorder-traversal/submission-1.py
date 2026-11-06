class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        trav_arr = []
        d = 0
        i = 0
        run = ""
        while i < len(traversal):
            if traversal[i] == '-':
                trav_arr.append([int(run), d])
                d = 0
                run = ""
                while traversal[i] == '-':
                    i += 1
                    d += 1
            else:
                run += traversal[i]
                i += 1
        else:
            trav_arr.append([int(run), d])
        depth_val = trav_arr[0]
        root = TreeNode(depth_val[0])
        st = [[root, depth_val]]
        for i in range(1, len(trav_arr)):
            cur_val, cur_depth = trav_arr[i]
            while st[-1][1][1] >= cur_depth:
                st.pop()
            cur_node = TreeNode(cur_val)
            if st[-1][0].left:
                st[-1][0].right = cur_node
                st.pop()
            else:
                st[-1][0].left = cur_node
            st.append([cur_node, trav_arr[i]])
        return root
