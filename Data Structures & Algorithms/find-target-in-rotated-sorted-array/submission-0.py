class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < nums[n - 1]:
                if target > nums[m] and target <= nums[n - 1]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] and target >= nums[0]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

        