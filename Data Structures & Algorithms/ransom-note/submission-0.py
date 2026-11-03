class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        magct = defaultdict(int)
        ranct = defaultdict(int)
        for i in ransomNote:
            ranct[i] += 1
        for i in magazine:
            magct[i] += 1
        for i, v in ranct.items():
            if magct[i] < v:
                return False
        return True

            
        