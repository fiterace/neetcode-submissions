class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        ans = []
        for i in range(n):
            ans.append(word1[i])
            ans.append(word2[i])
        return "".join(ans) + word1[n:] + word2[n:]