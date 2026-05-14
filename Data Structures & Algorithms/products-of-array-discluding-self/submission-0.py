class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_prod = 1
        num_0 = 0
        for num in nums:
            num_0 += not num
            all_prod *= num if num else 1
        print(num_0, all_prod)
        if num_0 > 1:
            return [0 for num in nums]

        ans = []
        for i in nums:
            ans.append((0 if num_0 else all_prod // i) if i else all_prod)
        return ans
        