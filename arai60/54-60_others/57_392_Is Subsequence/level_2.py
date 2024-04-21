# ポインタを2つ用意して、同じ文字ならsを次に進める
# while文で記載
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_index = 0
        s_index = 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        return s_index == len(s)


# DPで最長共通部分列問題を解く
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # longest_common_nums[i][j]はs[:i]とt[:j]の最長共通部分列の長さ
        longest_common_nums = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    longest_common_nums[i + 1][j + 1] = (
                        longest_common_nums[i][j] + 1
                    )
                    continue
                longest_common_nums[i + 1][j + 1] = max(
                    longest_common_nums[i + 1][j],
                    longest_common_nums[i][j + 1],
                )
        return longest_common_nums[-1][-1] == len(s)
