# 括弧内の計算を再帰的に行う
class Solution:
    def calculate(self, s: str) -> int:
        def helper_calculate(index):
            result = 0
            num = 0
            sign = 1
            while index < len(s):
                if s[index].isdigit():
                    num = num * 10 + int(s[index])
                if s[index] == "+":
                    result += num * sign
                    num = 0
                    sign = 1
                if s[index] == "-":
                    result += num * sign
                    num = 0
                    sign = -1
                if s[index] == ")":
                    result += num * sign
                    return index, result
                if s[index] == "(":
                    index, result_in_brackers = helper_calculate(index + 1)
                    result += result_in_brackers * sign
                index += 1
            result += num * sign
            return result

        return helper_calculate(0)
