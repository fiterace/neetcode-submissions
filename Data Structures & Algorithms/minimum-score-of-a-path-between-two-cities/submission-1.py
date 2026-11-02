from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u,v,w in roads:
            adjList[u].append((v,w))
            adjList[v].append((u,w))

        visited = [0]*(n+1)  
        score = float('inf')
        dfs = [1]
        while dfs:
            top = dfs.pop()
            if visited[top]:
                continue
            visited[top] = 1
            for v,w in adjList[top]:
                score = min(score, w)
                dfs.append(v)

        return int(score)