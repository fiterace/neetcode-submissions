class Solution:
    def rob(self, nums: List[int]) -> int:
        wo = 0
        for i in range(1,len(nums)):
            temp = wo
            wo = max(nums[0],wo)
            nums[0] = temp + nums[i]
        return max(nums[0],wo)