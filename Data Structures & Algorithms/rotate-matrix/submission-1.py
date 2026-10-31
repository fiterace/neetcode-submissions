class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        nj = n
        for i in range(n // 2): # till middle
            for j in range(i, nj - 1): # for every row we travel 1 less from the end
                # 0, 1 -> i, j
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i] # 0, 1 -> n - 1 - 1, 0
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j] # 0, 1 -> n - 1 - 0, n - 1 - 1 
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = temp
            nj -= 1