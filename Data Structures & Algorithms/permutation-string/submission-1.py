class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        window_size = len(s1)
        window_count = [0]*26
        count_s1 = [0]*26
        
        for i in s1:
            count_s1[ord(i) - ord('a')] += 1
        
        for i in range(window_size):
            window_count[ord(s2[i]) - ord('a')] += 1

        i = 0
        j = window_size
        while j < len(s2):
            if count_s1 == window_count:
                return True
            window_count[ord(s2[i]) - ord('a')] -= 1
            window_count[ord(s2[j]) - ord('a')] += 1
            i += 1
            j += 1
        
        return count_s1 == window_count
        