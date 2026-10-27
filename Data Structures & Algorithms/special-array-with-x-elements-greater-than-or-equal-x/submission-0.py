class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] >= n - i:
                return n - i
            i += 1
        return -1
