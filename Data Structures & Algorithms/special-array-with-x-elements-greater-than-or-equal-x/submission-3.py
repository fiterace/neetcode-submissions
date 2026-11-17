class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        ct = [0] * (n + 1)
        for i in nums:
            ct[min(i,n)] += 1
        run = 0
        for i in range(n,0,-1):
            run += ct[i]
            if i == run:
                return i
        return -1
        