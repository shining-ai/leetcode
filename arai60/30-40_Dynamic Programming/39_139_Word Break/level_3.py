class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def is_segmented(index):
            if index == len(s):
                return True
            for word in wordDict:
                if s[index : index + len(word)] != word:
                    continue
                if is_segmented(index + len(word)):
                    return True
            return False

        return is_segmented(0)
