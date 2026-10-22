class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for i,j in walls:
            grid[i][j] = 1
        for i,j in guards:
            grid[i][j] = 3
        ans = 0
        for guard in guards:
            i = guard[0]
            j = guard[1]
            
            for p,q in [[0,1],[0,-1],[1,0],[-1,0]]:
                x = i
                y = j
                while (x >= 0 and x < m and y >= 0 and y < n):
                    x = x + p
                    y = y + q
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 1 or grid[x][y] == 3:
                        break
                    if grid[x][y] == 2:
                        continue
                    else:
                        grid[x][y] = 2
                        ans += 1
        return m * n - len(guards) - len(walls) - ans
                
