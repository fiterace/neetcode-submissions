class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        cur = [0] * (n + 1)
        for a in text1:
            prev = 0
            for j, b in enumerate(text2, 1): # j goes from 1 -> n
                temp = max(max(cur[j-1], cur[j]), prev + 1) if a == b else max(cur[j-1], cur[j])
                prev = cur[j]
                cur[j] = temp
        return cur[-1]
            
