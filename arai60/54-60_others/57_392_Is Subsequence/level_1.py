# ポインタを2つ用意して、同じ文字ならsを次に進める
# sが最後まで進めばSubsequenceが存在する
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_index = 0
        for s_index in range(len(s)):
            if len(t) <= t_index:
                return False
            while t[t_index] != s[s_index]:
                t_index += 1
                if len(t) == t_index:
                    return False
            t_index += 1
        return True
