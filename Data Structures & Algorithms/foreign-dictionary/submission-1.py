from collections import deque, defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = {ch: 0 for w in words for ch in w}

        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    if y not in adj[x]:
                        adj[x].add(y)
                        indegree[y] += 1
                    break
            else:
                # no mismatch: invalid only if a is longer than b
                if len(a) > len(b):
                    return ""

        queue = deque(ch for ch, d in indegree.items() if d == 0)
        order = []
        while queue:
            ch = queue.popleft()
            order.append(ch)
            for nei in adj[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return "".join(order) if len(order) == len(indegree) else ""