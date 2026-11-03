class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = 0
        r = sum(nums)
        while l < r:
            m = (l + r)//2
            pos = True
            dk = k
            run = 0
            for i in nums:
                if run + i > m:
                    dk -= 1
                    run = i
                else:
                    run += i
                if dk == 0 or run > m:
                    pos = False
                    break
            if pos:
                r = m
            else:
                l = m + 1
        return l
        
        