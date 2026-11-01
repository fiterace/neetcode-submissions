class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        from heapq import heappush, heappop
        heap, total, ans = [], 0, 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heappush(heap, s)
            total += s
            if len(heap) > k:
                total -= heappop(heap)
            ans = max(ans, total * e)
        return ans % (10**9 + 7)