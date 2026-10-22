class Solution:
    def searchMatrix(self, arr: List[List[int]], tar: int) -> bool:
        m = len(arr)
        n = len(arr[0])
        r = j = m*n
        l = i = 0
        while(i < j):
            k = (i + j) // 2
            if(arr[(k+1)//m][(k+1)%m] == tar):
                return True
            elif(arr[k//m][k%m] > tar):
                j = k - 1
            else:
                i = k + 1
        return False
        