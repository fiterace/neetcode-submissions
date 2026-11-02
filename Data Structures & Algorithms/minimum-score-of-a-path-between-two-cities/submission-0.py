from collections import defaultdict
class Solution:
    visited = []
    score = float('inf')

    def bfs(self, i, adjList):
        if self.visited[i]:
            return
        self.visited[i] = 1
        for v,w in adjList[i]:
            self.score = min(self.score, w)
            self.bfs(v,adjList)



    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u,v,w in roads:
            adjList[u].append((v,w))
            adjList[v].append((u,w))

        self.visited = [0]*(n+1)  
        self.bfs(1,adjList)
        return self.score