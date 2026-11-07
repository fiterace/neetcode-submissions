class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        # odd length
        n = len(s)
        for i in range(n):
            k = 0
            while i - k >= 0 and i + k < n:
                if s[i - k] != s[i + k]:
                    break
                res += 1
                k += 1
        
        for i in range(n - 1):
            k = 0
            while i - k >= 0 and i + 1 + k < n:
                if s[i - k] != s[i + k + 1]:
                    break
                res += 1
                k += 1
        return res

        