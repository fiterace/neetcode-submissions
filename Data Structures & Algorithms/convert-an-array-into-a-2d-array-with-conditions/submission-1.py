class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ct = 1
        ans = [[nums[0]]]
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                ans[0].append(nums[i])
                ct = 1
            else:
                if len(ans) > ct:
                    ans[ct].append(nums[i])
                else:
                    ans.append([nums[i]])
                ct += nums[i] == nums[i - 1]
        return ans
