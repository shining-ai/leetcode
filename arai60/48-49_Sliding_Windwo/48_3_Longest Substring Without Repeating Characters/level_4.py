# 変数名を修正
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_last_index = {}
        left = 0
        max_length = 0
        for right, c in enumerate(s):
            if c in char_to_last_index:
                # leftより前の重複は無視する
                left = max(left, char_to_last_index[c] + 1)
            char_to_last_index[c] = right
            max_length = max(max_length, right - left + 1)
        return max_length
