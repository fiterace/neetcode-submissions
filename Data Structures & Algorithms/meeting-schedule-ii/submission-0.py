"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        all_times = [[i.start, 1] for i in intervals]
        all_times.extend([[i.end, -1] for i in intervals])
        rooms = 0
        ans = 0
        all_times.sort()
        for i, j in all_times:
            rooms += j
            ans = ans if ans > rooms else rooms
        return ans

        