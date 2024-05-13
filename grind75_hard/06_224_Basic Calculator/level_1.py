# 数字符号も含め10進数に直して、最後に全部足し算する
# ()で囲まれた部分を先に計算するため、stackに入れておく
# 各文字に対する処理をそれぞれ記載
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        num = 0
        for c in s:
            if c.isspace():
                continue
            if c.isdigit():
                num = num * 10 + int(c)
                continue
            if c == "(":
                stack.append((c, sign))
                sign = 1
                continue
            if c == "-":
                stack.append((num, sign))
                sign = -1
            if c == "+":
                stack.append((num, sign))
                sign = 1
            if c == ")":
                num *= sign
                while 1:
                    expression, sign = stack.pop()
                    if expression == "(":
                        break
                    num += expression * sign
                stack.append((num, sign))
            num = 0
        if num != 0:
            stack.append((num, sign))
        result = 0
        for num, sign in stack:
            result += num * sign
        return result
