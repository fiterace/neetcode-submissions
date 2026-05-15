class Solution:
    def trap(self, height: List[int]) -> int:
        store = []
        ans = 0
        for i in height:
            ans = max(ans, i)
            store.append(ans)
        
        print(store)
        ans = 0
        water = 0
        for i in range(len(height) - 1, 0, -1):
            ans = max(ans, height[i])
            water += max(0, min(store[i], ans) - height[i])
            print(i, water)
        
        return water

        