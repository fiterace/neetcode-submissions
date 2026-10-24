class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        steps = [n, m - 1]          # [horizontal, vertical]
        i, j = 0, -1
        di, dj = 0, 1
        ans = []
        k = 0
        while steps[k % 2] > 0:
            for _ in range(steps[k % 2]):
                i += di
                j += dj
                ans.append(matrix[i][j])
            steps[k % 2] -= 1
            di, dj = dj, -di        # turn right: R -> D -> L -> U
            k += 1
        return ans