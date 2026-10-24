class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        time = intervals[0][1]
        ans = 0
        for i,j in intervals[1:]:
            if i < time:
                ans += 1
                time = min(time,j)
                continue
            time = j
        return ans