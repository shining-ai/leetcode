# ポインタを2つ用意して、同じ文字ならsを次に進める
# sが最後まで進めばSubsequenceが存在する
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_index = 0
        for s_index in range(len(s)):
            for t_index in range(t_index, len(t)):
                if t[t_index] == s[s_index]:
                    t_index += 1
                    break
            else:
                return False
        return True


# 正規表現
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pattern = ""
        for c in s:
            pattern += ".*" + c
        return re.match(pattern, t) != None
