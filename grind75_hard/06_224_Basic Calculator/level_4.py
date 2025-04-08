# 再帰下降構文解析
class Solution:
    def calculate(self, s: str) -> int:
        index = 0

        def get_next_expression():
            nonlocal index
            index += 1
            while index < len(s) and s[index].isspace():
                index += 1

        def expr():
            nonlocal index
            result = factor()
            while index < len(s) and s[index] in "+-":
                op = s[index]
                get_next_expression()
                if op == "+":
                    result += factor()
                else:
                    result -= factor()
            return result

        def factor():
            nonlocal index
            result = 0
            while index < len(s) and s[index].isdigit():
                result = 10 * result + int(s[index])
                get_next_expression()
            if index < len(s) and s[index] == "(":
                get_next_expression()
                result = expr()
                get_next_expression()  # ")"を読み飛ばす
            return result

        if index < len(s) and s[0].isspace():
            get_next_expression()
        return expr()
