class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        ans = 0
        n = len(coins)
        dp = [[0 for i in range(amount + 1)] for i in range(n)]

        def coin_change_recursive(coins, amount, i, n, dp):
            if not amount:
                return 0
            if i >= n:
                return -1
            if dp[i][amount]:
                return dp[i][amount]
            taken = -1
            if coins[i] <= amount:
                taken = coin_change_recursive(coins, amount - coins[i], i, n, dp)
            wo = coin_change_recursive(coins, amount, i + 1, n, dp)
            if taken != -1 and wo != -1:
                dp[i][amount] = min(taken + 1, wo)
            elif taken != -1:
                dp[i][amount] = taken + 1
            else:
                dp[i][amount] = wo
            return dp[i][amount]
        
        return coin_change_recursive(coins, amount, 0, n, dp)

