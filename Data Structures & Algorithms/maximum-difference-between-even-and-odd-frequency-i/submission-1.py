class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        cts = Counter(s)
        odd = 0
        even = len(s)
        for i, v in cts.items():
            if v%2:
                odd = max(odd, v)
            else:
                even = min(even, v)
        return odd - even



        