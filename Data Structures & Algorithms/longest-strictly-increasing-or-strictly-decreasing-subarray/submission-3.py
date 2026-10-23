class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        dec = 1
        inc = 1
        prev = nums[0]
        ans = 1
        for i in range(1,len(nums)):
            if nums[i] > prev:
                inc += 1
                dec = 1
            elif nums[i] < prev:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            prev = nums[i]
            ans = max(inc,dec,ans)
        return ans

        