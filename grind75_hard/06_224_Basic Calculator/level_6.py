# 再帰下降構文解析
# スペースを最初に除去
# result = 0のタイミングを修正
# 単行演算子を明示的に処理
class Solution:
    def calculate(self, s: str) -> int:
        index = 0

        def expr():
            nonlocal index
            if index < len(s) and s[index] == "-":
                index += 1
                result = -factor()
            else:
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
            if index < len(s) and s[index] == "(":
                index += 1
                result = expr()
                index += 1  # ")"を読み飛ばす
                return result
            result = 0
            while index < len(s) and s[index].isdigit():
                result = 10 * result + int(s[index])
                index += 1
            return result

        s = s.replace(" ", "")
        return expr()
