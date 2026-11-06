class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n
        while l < r:
            m = (l + r + 1) // 2
            val = m*(m + 1) // 2
            if val > n:
                r = m - 1
            else:
                l = m
        return l
        