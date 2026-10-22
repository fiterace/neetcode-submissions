class Solution:
    def searchMatrix(self, arr: List[List[int]], tar: int) -> bool:
        m, n = len(arr), len(arr[0])
        i, j = 0, m * n - 1
        while i <= j:
            k = (i + j) // 2
            val = arr[k // n][k % n]
            if val == tar:
                return True
            elif val > tar:
                j = k - 1
            else:
                i = k + 1
        return False