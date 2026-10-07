class Solution:
    def add(self,a,b):
        return a + b
    
    def mul(self,a,b):
        return a * b
    
    def sub(self,a,b):
        return a - b

    def div(self,a,b):
        return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = {'+': self.add,'-': self.sub,'*': self.mul,'/': self.div}
        for i in tokens:
            if i not in operators:
                st.append(int(i))
            else:
                new = operators[i](st[-2],st[-1])
                st.pop()
                st.pop()
                st.append(new)
        return st[-1]

            
        