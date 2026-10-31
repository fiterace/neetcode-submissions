class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        m, n = len(mat), len(mat[0])
        first_row = 0 # bool 1 if any in row 0
        first_col = 0 # bool 1 if any in col 0

        for i in range(m):
            if mat[i][0] == 0:
                first_col = 1
        
        for i in range(n):
            if mat[0][i] == 0:
                first_row = 1
        
        if mat[0][0] == 0:
            first_col = first_row = 1

        for i in range(1,m):
            for j in range(1,n):
                if mat[i][j] == 0:
                    mat[i][0] = mat[0][j] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        
        if first_col:
            for i in range(m):
                mat[i][0] = 0
        
        if first_row:
            for i in range(n):
                mat[0][i] = 0