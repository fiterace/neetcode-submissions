from collections import deque, defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # building the graph
        adj_list = defaultdict(set)
        n = len(words)
        letters = set()
        for w in words:
            for ch in w:
                letters.add(ch)

        for i in range(n):
            for j in range(i + 1,n):
                a = words[i]
                b = words[j]
                c = min(len(a),len(b))
                x = 0
                while x < c:
                    if(a[x] != b[x]):
                        adj_list[a[x]].add(b[x])
                        break
                    x += 1
                else:
                    if len(a) > len(b):
                        return ""
        print(adj_list)
        # topological sort
        # 1 getting indegrees
        indegree = {x: 0 for x in letters}
        for i,v in adj_list.items():
            for x in v:
                indegree[x] += 1
        print(indegree)
        # 2 getting started
        kahn_que = deque()
        for i,v in indegree.items():
            if(v == 0):
                kahn_que.append(i)
        
        order = []
        while kahn_que:
            top = kahn_que.popleft()
            order.append(top)
            for padosi in adj_list[top]:
                indegree[padosi] -= 1
                if(indegree[padosi] == 0):
                    kahn_que.append(padosi)
        print(order, len(order), len(letters))
        final_order = order if len(order) == len(letters) else None
        if not final_order:
            return ""
        ans = "".join(order)
        return ans
        


        