class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        sign = 1
        value = 0
        finish_space = False
        finish_sign = False
        for c in s:
            if not finish_space and c.isspace():
                continue
            finish_space = True
            if not finish_sign and (c == "+" or c == "-"):
                if c == "-":
                    sign = -1
                finish_sign = True
                continue
            finish_sign = True
            if "0" <= c <= "9":
                digit = ord(c) - ord("0")
                value *= 10
                value += sign * digit
                if INT_MIN > value:
                    return INT_MIN
                if value > INT_MAX:
                    return INT_MAX
                continue
            break
        return value
