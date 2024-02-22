# それぞれの文字の出現回数を数えておく
# 1度だけ出現する文字が答え
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        return -1


# 1文字ずつ同じ文字が出現しないか確認する
# 手作業でやるとしたらこういう感じ
class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        for i, c_checking in enumerate(s):
            if c_checking in visited:
                continue
            for c in s[i + 1 :]:
                if c_checking == c:
                    visited.add(c_checking)
                    break
            else:
                return i
        return -1
