class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        ans = 1
        count = 1
        cur = nums[0]
        for num in nums:
            if num == cur:
                continue
            elif num == cur + 1:
                count += 1
                cur = num
            else:
                cur = num
                count = 1
            ans = max(count, ans)
        return ans
            