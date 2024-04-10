# Brute Force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i, base_c in enumerate(s):
            seen = set(base_c)
            length = 1
            for c in s[i + 1 :]:
                if c in seen:
                    break
                seen.add(c)
                length += 1
            max_length = max(max_length, length)
        return max_length


# Sliding Window
# 一度出てきた文字のindexを記録して、leftの位置の更新に計算を不要にする
# abcade
# 同じ文字が出現した場合 right = 3: abca → 文字の長さは(right - left)となる
# rightが走りきった場合 right = 5: bcdae → 文字の長さは(right - left + 1)となる
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen_index = {}
        left = 0
        max_length = 0
        for right, c in enumerate(s):
            if c in seen_index:
                max_length = max(max_length, right - left)
                left = max(left, seen_index[c] + 1)
            seen_index[c] = right
        max_length = max(max_length, right - left + 1)
        return max_length
