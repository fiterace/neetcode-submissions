class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        m, n = len(s), len(t)
        # no of ways t[:j] -> subsequence of s[:i] = dp[i][j]
        # if si == tj -> dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        # else: dp[i][j] = dp[i-1][j]
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1,m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    if j <= i:
                        dp[i][j] = (dp[i - 1][j - 1] if i > 1 and j > 1 else 1) + dp[i - 1][j]
                    else:
                        dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[-1][-1]

