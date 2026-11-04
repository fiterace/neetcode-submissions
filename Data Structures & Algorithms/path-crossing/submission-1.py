class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dic = {'N': (-1,0), 'S': (1,0), 'E': (0,1), 'W': (0,-1)}
        x = 0
        y = 0
        visited = set([(0,0)])
        for i in path:
            dx, dy = dic[i]
            if (x + dx, y + dy) in visited:
                return True
            x += dx
            y += dy
            visited.add((x,y))
        return False

        