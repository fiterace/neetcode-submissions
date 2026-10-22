class Solution:
    def rob(self, nums: List[int]) -> int:
        wo = 0
        take = nums[0]
        for i in range(1,len(nums)):
            temp = wo
            wo = max(take,wo)
            take = temp + nums[i]
        return max(take,wo)