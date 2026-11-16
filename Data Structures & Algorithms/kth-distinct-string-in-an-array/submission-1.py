from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ct = Counter(arr)
        for s in arr:
            if ct[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""