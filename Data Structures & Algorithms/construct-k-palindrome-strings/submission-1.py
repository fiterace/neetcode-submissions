class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        from collections import Counter
        cts = Counter(s)
        odds = 0
        for i, v in cts.items():
            if v%2:
                odds += 1
        return True if odds <= k and k <= len(s) else False
