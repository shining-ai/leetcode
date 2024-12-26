# ポインタを2つ使い条件を満たす範囲を見つける。
# まずtの文字全てが含まれるwindowを見つけるために、rightを進めていく
# tの文字全てが含まれるwindowを見つけたら、leftを進めて無駄な文字を削除していく
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        window_count = defaultdict(int)
        left = 0
        right = 0
        match_num = 0
        min_length = math.inf, None, None
        while right < len(s):
            if s[right] in t_count:
                window_count[s[right]] += 1
                if window_count[s[right]] == t_count[s[right]]:
                    match_num += 1
            while left <= right and match_num == len(t_count):
                if min_length[0] > right - left:
                    min_length = right - left, left, right
                if s[left] in t_count:
                    window_count[s[left]] -= 1
                    if window_count[s[left]] < t_count[s[left]]:
                        match_num -= 1
                left += 1
            right += 1
        if min_length[0] == math.inf:
            return ""
        _, left, right = min_length
        return s[left : right + 1]
