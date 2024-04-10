class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = 0
        max_length = 0
        seen_char_index = {}
        for end, c in enumerate(s):
            if c in seen_char_index:
                begin = max(begin, seen_char_index[c] + 1)
            seen_char_index[c] = end
            max_length = max(max_length, end - begin + 1)
        return max_length
