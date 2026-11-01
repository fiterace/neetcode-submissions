class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        ans = 0
        n = len(coins)
        dp = [0] + [float('inf') for i in range(amount)]
        # Recursion time was better so maybe not use this solution, but recursion can have max recursion issue
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1