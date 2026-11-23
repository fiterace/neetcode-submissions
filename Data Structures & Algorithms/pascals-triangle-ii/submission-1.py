class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1,1] if rowIndex else [1]
        prev = [0,1,1,0]
        for i in range(2, rowIndex + 1):
            new = [0]
            tmp = prev[0]
            for i in prev[1:]:
                new.append(tmp + i)
                tmp = i
            new.append(0)
            prev = list(new)
        return prev[1:-1]
        