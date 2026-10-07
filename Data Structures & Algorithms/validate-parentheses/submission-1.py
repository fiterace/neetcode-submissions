class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        match = {'{':'}','[':']','(':')'}
        for i in s:
            if i in ['{','(','[']:
                st.append(i)
            else:
                if len(st) and match[st[-1]] == i:
                    st.pop()
                else:
                    return False
        return False if len(st) else True