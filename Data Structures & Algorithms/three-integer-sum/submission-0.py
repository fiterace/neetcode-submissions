class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        def binary_search(i, tar):
            j = len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if(nums[m] == tar):
                    return m
                elif nums[m] > tar:
                    j = m - 1
                else:
                    i = m + 1
            return -1

        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                tar = 0 - nums[i] - nums[j]
                k = binary_search(j + 1, tar)
                if k != -1:
                    ans.add((nums[i],nums[j],nums[k]))
        
        return list(ans)