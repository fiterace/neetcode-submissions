class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        ans = 0
        for i in coins:
            if not amount:
                return ans
            ans += (amount//i)
            amount = amount%i
        return ans if not amount else -1
        