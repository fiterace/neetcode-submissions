class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        store = set(nums)
        ans = 1
        for num in nums:
            if num - 1 in store:
                continue
            else:
                cur = num + 1
                count = 1
                while cur in store:
                    cur += 1
                    count += 1
                ans = max(ans, count)
        return ans