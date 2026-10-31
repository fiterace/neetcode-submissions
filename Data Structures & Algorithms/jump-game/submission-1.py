class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0
        n = len(nums)
        for i in range(0,n):
            if i <= max_i:
                max_i = max(max_i, i + nums[i])
            if max_i >= n - 1:
                return True
        return max_i >= n - 1