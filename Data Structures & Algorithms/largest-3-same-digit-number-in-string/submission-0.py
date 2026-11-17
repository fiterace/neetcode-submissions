class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = ""
        for i in range(n-2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                if (ans and int(ans) < int(num[i:i+3])) or ans == "":
                    ans = num[i:i+3]
        return ans

        