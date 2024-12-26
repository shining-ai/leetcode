# 変数名の修正
# defaultdectを[0]*128に変更
# tに含まれていない文字もカウントするように修正
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        num_chars_in_t = [0] * 128
        for c in t:
            num_chars_in_t[ord(c)] += 1
        num_needed_matches = 128 - num_chars_in_t.count(0)
        left = 0
        num_matches = 0
        num_chars_in_window = [0] * 128
        min_window_index = (left, len(s))
        for right, c in enumerate(s):
            num_chars_in_window[ord(c)] += 1
            if num_chars_in_window[ord(c)] == num_chars_in_t[ord(c)]:
                num_matches += 1
            while left <= right and num_matches == num_needed_matches:
                if right - left + 1 < min_window_index[1] - min_window_index[0] + 1:
                    min_window_index = (left, right)
                num_chars_in_window[ord(s[left])] -= 1
                if num_chars_in_window[ord(s[left])] < num_chars_in_t[ord(s[left])]:
                    num_matches -= 1
                left += 1
        min_window_left, min_window_right = min_window_index
        if min_window_right == len(s):
            return ""
        return s[min_window_left : min_window_right + 1]
