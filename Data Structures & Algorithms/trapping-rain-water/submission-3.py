class Solution:
    def trap(self, height: List[int]) -> int:
        from collections import deque
        st = deque()
        i = 0
        ans = 0
        for i in range(len(height)):
            while(len(st) and height[i] > height[st[-1]]):
                bottom = height[st.pop()]
                if(len(st)):
                    left = height[st[-1]]
                    right = height[i]
                    h = min(left, right) - bottom
                    w = i - st[-1] - 1
                    ans += h*w
            st.append(i)
        
        return ans


        