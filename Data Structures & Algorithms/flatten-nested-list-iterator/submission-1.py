class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.st = nestedList[::-1]

    def next(self) -> int:
        self.hasNext()
        return self.st.pop().getInteger()
        
    def hasNext(self) -> bool:
        while self.st:
            top = self.st[-1]
            if top.isInteger():
                return True
            top = self.st.pop()
            self.st.extend(top.getList()[::-1])
        return False 
        
