# 再帰下降構文解析
class Solution:
    def calculate(self, s: str) -> int:
        index = 0

        def expr():
            nonlocal index
            result = factor()
            while index < len(s) and s[index] in "+-":
                op = s[index]
                index += 1
                if op == "+":
                    result += factor()
                else:
                    result -= factor()
            return result

        def factor():
            nonlocal index
            result = 0
            if index < len(s) and s[index] == "(":
                index += 1
                result = expr()
                index += 1  # ")"を読み飛ばす
                return result
            while index < len(s) and s[index].isdigit():
                result = 10 * result + int(s[index])
                index += 1
            return result

        s = s.replace(" ", "")
        return expr()
