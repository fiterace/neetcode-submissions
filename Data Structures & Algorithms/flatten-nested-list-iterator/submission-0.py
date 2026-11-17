class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        def flatten(arr):
            normal_list = []
            for a in arr:
                if a.isInteger():
                    normal_list.append(a.getInteger())
                else:
                    normal_list.extend(flatten(a.getList()))
            return normal_list
        self.new_list = flatten(nestedList)
        self.n = len(self.new_list)
        self.it = 0

    def next(self) -> int:
        self.it += 1
        return self.new_list[self.it - 1]
        
    def hasNext(self) -> bool:
        return self.it < self.n
