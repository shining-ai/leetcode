# 1文字進むごとに今の長さを調べることで、条件を減らした
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_char_index = {}
        begin = 0
        max_length = 0
        for end, c in enumerate(s):
            if c in seen_char_index:
                # beginより前の重複は無視する
                begin = max(begin, seen_char_index[c] + 1)
            seen_char_index[c] = end
            max_length = max(max_length, end - begin + 1)
        return max_length
