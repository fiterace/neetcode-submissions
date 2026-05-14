class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert_to_map(word: str):
            ans = [0 for i in range(26)]
            for i in word:
                ans[ord(i) - ord('a')] += 1
            return ans

        ans = []
        for x in strs:
            ans.append([x,convert_to_map(x)])
        
        ans.sort(key = lambda x: x[1])

        prev = ans[0]
        ans2 = [[prev[0]]]
        i = 1
        for cur in ans:
            if i:
                i = 0
                continue
            if cur[1] == prev[1]:
                ans2[-1].append(cur[0])
            else:
                ans2.append([cur[0]])
            prev = cur
        return ans2

            

        