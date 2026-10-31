class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        mins = []
        n = len(prices)
        for i in range(n-1,-1,-1):
            while len(mins) and mins[-1] > prices[i]:
                mins.pop()

            if len(mins) and mins[-1] <= prices[i]:
                prices[i] -= mins[-1]
            mins.append(prices[i])
        return prices
        

