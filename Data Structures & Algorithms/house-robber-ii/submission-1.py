class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_line(nums, 0, len(nums) - 1),   # skip last house
                   self.rob_line(nums, 1, len(nums)))       # skip first house

    def rob_line(self, nums, start, end):
        skip, take = 0, 0          # best if we skip / rob the current house
        for i in range(start, end):
            skip, take = max(skip, take), skip + nums[i]
        return max(skip, take)