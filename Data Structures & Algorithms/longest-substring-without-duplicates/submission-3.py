class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = -1
        pos = {}
        ans = 0
        for i in range(len(s)):
            left = pos.get(s[i], -1)
            if left > start:
                start = left
            ans = max(ans, i - start)
            print(i, start, left , ans)
            pos[s[i]] =  i
        return ans