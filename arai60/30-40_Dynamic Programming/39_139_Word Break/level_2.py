# Bottom-up DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        segmented = [False] * (len(s) + 1)
        segmented[0] = True
        for end in range(1, len(s) + 1):
            for start in range(end):
                if not segmented[start]:
                    continue
                if s[start:end] in wordDict:
                    segmented[end] = True
        return segmented[-1]
