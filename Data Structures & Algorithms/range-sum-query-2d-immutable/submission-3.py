class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        m, n = len(self.mat), len(self.mat[0])
        self.sum_mat = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.sum_mat[i][j] = self.sum_mat[i][j - 1] + self.sum_mat[i - 1][j] - self.sum_mat[i - 1][j - 1] + self.mat[i - 1][j - 1]

    def sumRegion(self, i: int, j: int, x: int, y: int) -> int:
        i, j, x, y = i + 1, j + 1, x + 1, y + 1
        return self.sum_mat[x][y] + self.sum_mat[i - 1][j - 1] - self.sum_mat[x][j-1] - self.sum_mat[i - 1][y]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)