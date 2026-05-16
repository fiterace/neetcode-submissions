class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        store = [0]*26
        i = j = ans = 0 
        while j < len(s) or i < len(s):
            print(i,j,ans,j - i - store[ord(s[i]) - ord('A')],store)
            k_use = j - i - store[ord(s[i]) - ord('A')]
            if k_use > k:
                store[ord(s[i]) - ord('A')] -= 1
                i += 1
            elif j == len(s):
                ans = max(ans, min(j - i + k - k_use, len(s)))
                store[ord(s[i]) - ord('A')] -= 1
                i += 1
            elif k_use == k and s[j] != s[i]:
                store[ord(s[i]) - ord('A')] -= 1
                i += 1
            else:
                store[ord(s[j]) - ord('A')] += 1
                k_use += 1 if s[j] != s[i] else 0
                j += 1
                ans = max(ans, min(j - i + k - k_use, len(s)))           
        return ans