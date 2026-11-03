class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i = 0
        j = len(tokens) - 1
        tokens.sort()
        score = 0
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                i += 1
                score += 1
            elif score and i < j:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        return score