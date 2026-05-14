class Solution:

    key = "87tr c32qb78ety89rycb387oceycp 87vy 9r7y"
    key2 = "nfwiudh 9*Y*& edtWb6tu9iHG*&T *67t*&To8 yugx8&"

    def encode(self, strs: List[str]) -> str:
        from functools import reduce
        return reduce(lambda x,y: x + self.key + y, strs) if len(strs) > 1 else ((strs[0] if strs[0] else self.key2) if strs else "")
        

    def decode(self, s: str) -> List[str]:
        return (s.split(self.key) if s else []) if s != self.key2 else [""]
