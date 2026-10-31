class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False for i in nums]
        n = len(nums)
        can_reach[0] = True
        for i in range(n):
            if can_reach[i] and i + nums[i] < n:
                can_reach[i + nums[i]] = True
        return can_reach[-1]