from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.right and num <= self.right[0]:
            heappush(self.left, -1*num)
        else:
            heappush(self.right, num)
        if len(self.left) < len(self.right):
            top = heappop(self.right)
            heappush(self.left, -1*top)
        elif len(self.left) - len(self.right) > 1:
            top = -1*heappop(self.left)
            heappush(self.right, top)

    def findMedian(self) -> float:
        return -1*self.left[0] if len(self.left) > len(self.right) else (-1*self.left[0] + self.right[0])/2