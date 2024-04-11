# 1文字進むごとに今の長さを調べることで、条件を減らした
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_char_index = {}
        left = 0
        max_length = 0
        for right, c in enumerate(s):
            if c in seen_char_index:
                # leftより前の重複は無視する
                left = max(left, seen_char_index[c] + 1)
            seen_char_index[c] = right
            max_length = max(max_length, right - left + 1)
        return max_length
