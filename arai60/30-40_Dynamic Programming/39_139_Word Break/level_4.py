# Bottom-up DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_length = len(max(wordDict, key=len))
        segmented = [False] * (len(s) + 1)
        segmented[0] = True
        for end in range(1, len(s) + 1):
            for start in range(max(0, end - max_length), end):
                if not segmented[start]:
                    continue
                if s[start:end] in wordDict:
                    segmented[end] = True
        return segmented[-1]
