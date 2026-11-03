class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans += 4
                    if i - 1 >= 0 and grid[i - 1][j]:
                        ans -= 2
                    if j - 1 >= 0 and grid[i][j-1]:
                        ans -= 2
        return ans

        