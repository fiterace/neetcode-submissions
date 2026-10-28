class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[-1]
        i = 0
        j = n - 1
        while i < j:
            m = (i + j) // 2
            if (nums[m] < last):
                j = m
            elif(nums[m] > last):
                i = m + 1
        return nums[i]
        