# Top-Down DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def is_segmented(start):
            if start == len(s):
                return True
            for word in wordDict:
                if s[start : start + len(word)] != word:
                    continue
                if is_segmented(start + len(word)):
                    return True
            return False

        return is_segmented(0)


# BFS的に解く
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        index_queue = deque([0])
        seen = set()
        while index_queue:
            index = index_queue.popleft()
            if index in seen:
                continue
            for word in wordDict:
                next_index = index + len(word)
                if s[index:next_index] != word:
                    continue
                if len(s) == next_index:
                    return True
                index_queue.append(next_index)
            seen.add(index)
        return False
