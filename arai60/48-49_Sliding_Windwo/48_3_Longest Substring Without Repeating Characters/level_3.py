class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        seen_char_index = {}
        for right, c in enumerate(s):
            if c in seen_char_index:
                left = max(left, seen_char_index[c] + 1)
            seen_char_index[c] = right
            max_length = max(max_length, right - left + 1)
        return max_length
