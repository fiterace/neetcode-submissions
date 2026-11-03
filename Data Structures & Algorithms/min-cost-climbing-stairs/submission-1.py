class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_2 = 0
        cost_1 = 0
        for i in range(2, len(cost)):
            cost_1, cost_2 = min(cost_1 + cost[i - 1], cost_2 + cost[i - 2]), cost_1 
        return min(cost_1 + cost[-1], cost_2 + cost[-2])
        