# 再帰下降構文解析
class Solution:
    def calculate(self, s: str) -> int:
        index = 0

        def skip_spaces():
            nonlocal index
            index += 1
            while index < len(s) and s[index].isspace():
                index += 1

        def expr():
            nonlocal index
            result = factor()
            while index < len(s) and s[index] in "+-":
                op = s[index]
                skip_spaces()
                if op == "+":
                    result += factor()
                else:
                    result -= factor()
            return result

        def factor():
            nonlocal index
            result = 0
            if index < len(s) and s[index] == "(":
                skip_spaces()
                result = expr()
                skip_spaces()  # ")"を読み飛ばす
                return result
            while index < len(s) and s[index].isdigit():
                result = 10 * result + int(s[index])
                skip_spaces()
            return result

        if index < len(s) and s[0].isspace():
            skip_spaces()
        return expr()
