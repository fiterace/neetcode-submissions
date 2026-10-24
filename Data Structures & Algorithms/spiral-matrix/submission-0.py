class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        tot = m*n
        dx_arr = [[0,1,n],[1,0,m - 1],[0,-1,n - 1],[-1,0,m - 2]]
        i,j = 0,-1
        ans = []
        while len(ans) < tot:
            for dxi,dxj,dxl in dx_arr:
                for _ in range(dxl):
                    i += dxi
                    j += dxj
                    ans.append(matrix[i][j])
                    if len(ans) == tot:
                        break
                if len(ans) == tot:
                    break
            for itr in range(4):
                dx_arr[itr][2] -= 1
        return ans        