class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        m,n = len(a), len(a[0])
        for i in range(m):
            for j in range(n):
                if a[i][j] == 0:
                    a[i][0] = 0
                    a[0][j] = 0
        
        for i in range(m):
            if a[i][0] == 0:
                for j in range(n):
                    a[i][j] = 0
        for j in range(n):
            if a[0][j] == 0:
                for i in range(m):
                    a[i][j] = 0
        