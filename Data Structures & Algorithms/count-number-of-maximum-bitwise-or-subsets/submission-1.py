class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        from collections import defaultdict
        cts = defaultdict(int)
        n = len(nums)
        def recursion(i, ans):
            if i == n:
                cts[ans] += 1
                return
            recursion(i + 1, ans)
            recursion(i + 1, ans | nums[i])
        recursion(0,0)
        return cts[max(cts.keys())]

