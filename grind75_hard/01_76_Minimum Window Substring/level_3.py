class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        left = 0
        min_window_index = (left, math.inf)
        window_count = defaultdict(int)
        match_num = 0
        for right, c in enumerate(s):
            if c not in t_count:
                continue
            window_count[c] += 1
            if window_count[c] == t_count[c]:
                match_num += 1
            while left <= right and match_num == len(t_count):
                if right - left + 1 < min_window_index[1] - min_window_index[0] + 1:
                    min_window_index = (left, right)
                if s[left] in t_count:
                    window_count[s[left]] -= 1
                    if window_count[s[left]] < t_count[s[left]]:
                        match_num -= 1
                left += 1
        left, right = min_window_index
        if right == math.inf:
            return ""
        return s[left : right + 1]
