class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 1 if s[0] != '0' else 0
        dp = [[1 if s[0] != '0' else 0, 0],
            [0, 0]]

        def valid_char(x, y):
            num = int(f"{x}{y}")
            if x != '0' and num <= 26 and num >= 1:
                return True
            return False

        dp[0][1] = dp[0][0] + dp[1][0] if s[1] != '0' else 0
        dp[1][1] = 1 if valid_char(s[0],s[1]) else 0

        for i in range(2,n):
            dp[0][0] = dp[0][1]
            dp[1][0] = dp[1][1]

            dp[0][1] = dp[0][0] + dp[1][0] if s[i] != '0' else 0
            dp[1][1] = dp[0][0] if valid_char(s[i - 1], s[i]) else 0

        return dp[0][1] + dp[1][1]