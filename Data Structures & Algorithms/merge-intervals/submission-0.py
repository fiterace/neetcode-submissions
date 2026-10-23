class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        merged.append(intervals[0])
        for i,j in intervals:
            p,q = merged[-1]
            if (i<=q):
                if(j>q):
                    merged[-1][1] = j
            else:
                merged.append([i,j])
        return merged

        