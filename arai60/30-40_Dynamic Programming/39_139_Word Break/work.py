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
                next_start = start_index + len(word)
                if s[start_index:next_start] != word:
                    continue
                if next_start == len(s):
                    return True
                stack.append(next_start)
        return False
