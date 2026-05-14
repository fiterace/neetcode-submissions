class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from heapq import heapify
        sort = []
        heapq.heapify(sort)
        nums.sort()
        cur = nums[0]
        count = 0
        for num in nums:
            if num == cur:
                count+=1
            else:
                heapq.heappush(sort, [count, cur])
                cur = num
                count = 1
            while len(sort) > k:
                heapq.heappop(sort)
        heapq.heappush(sort, [count, cur])
        while len(sort) > k:
            heapq.heappop(sort)
        return [x[1] for x in sort]

        