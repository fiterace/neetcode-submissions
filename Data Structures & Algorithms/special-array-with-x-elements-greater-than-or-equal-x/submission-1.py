class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        while i < n:
            x = n - i
            if nums[i] >= x and (i == 0 or nums[i - 1] < x):
                return x
            i += 1
        return -1
