class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        profit = 0
        for i in prices:
            if i > buy and i > sell:
                sell = i
            elif i < buy:
                buy = i
                sell = i
            profit = max(profit, sell - buy)
        return profit