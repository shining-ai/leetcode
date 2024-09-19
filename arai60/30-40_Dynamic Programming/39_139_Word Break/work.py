# BFS的に解く
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        stack = [0]
        seen = set()
        while stack:
            start_index = stack.pop()
            if start_index in seen:
                continue
            seen.add(start_index)
            for word in wordDict:
                end_index = start_index + len(word)
                if s[start_index:end_index] != word:
                    continue
                if end_index == len(s):
                    return True
                stack.append(end_index)
        return False
