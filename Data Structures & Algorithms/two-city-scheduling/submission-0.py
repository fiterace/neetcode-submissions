class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1]) # sort by cheaper to send to a
        n = len(costs) // 2
        return sum(a for a,_ in costs[:n]) + sum(b for _, b in costs[n:])
