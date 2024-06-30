class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        return -1
