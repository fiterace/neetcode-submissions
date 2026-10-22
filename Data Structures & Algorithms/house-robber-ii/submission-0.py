class Solution:
    def rob(self, nums: List[int]) -> int:
        wo = 0
        take = nums[0]
        wo_not1 = 0
        take_not1 = 0
        for i in range(1,len(nums) - 1):
            temp = wo
            temp_not1 = wo_not1
            wo = max(wo,take)
            wo_not1 = max(wo_not1,take_not1)
            take = temp + nums[i]
            take_not1 = temp_not1 + nums[i]
        return max(take_not1, wo_not1 + nums[-1], take, wo)
