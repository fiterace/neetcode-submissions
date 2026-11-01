class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        prev = [0] * (n + 1)
        for a in text1:
            cur = [0]
            for j, b in enumerate(text2, 1): # j goes from 1 -> n
                temp = max(max(cur[j-1], prev[j]), prev[j - 1] + 1) if a == b else max(cur[j-1], prev[j])
                cur.append(temp)
            prev = cur
        return prev[-1]
            
