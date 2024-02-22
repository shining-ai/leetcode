# 1段目のコードから変更なし
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        return -1


# 1段目のコードのリファクタリング
# 2重ループをlistの検索で書き換えた
class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        for i, c_checking in enumerate(s):
            if c_checking in visited:
                continue
            if c_checking in s[i + 1 :]:
                visited.add(c_checking)
                continue
            return i
        return -1
