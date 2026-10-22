class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        arr = [[0,0] for i in range(n)]
        arr[0][0] = 0
        arr[0][1] = arr[1][0] = nums[0]
        arr[1][1] = nums[1]
        for i in range(2,n):
            arr[i][0] = max(arr[i - 1][0],arr[i - 1][1])
            arr[i][1] = arr[i - 1][0] + nums[i]
        return max(arr[-1][0],arr[-1][1])