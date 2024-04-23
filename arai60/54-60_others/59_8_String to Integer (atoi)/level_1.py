# スペース、符号、数字のチェックを順番に行っていく
# pythonはオーバーフローしないので、最後にチェックするだけにした
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        value = 0
        sign = 1
        index = 0
        while index < len(s) and s[index] == " ":
            index += 1
        if index < len(s) and (s[index] == "-" or s[index] == "+"):
            if s[index] == "-":
                sign *= -1
            index += 1
        while index < len(s) and "0" <= s[index] <= "9":
            digit = ord(s[index]) - ord("0")
            value *= 10
            value += digit
            index += 1
        value *= sign
        if -(2**31) <= value <= 2**31 - 1:
            return value
        if sign == -1:
            return -(2**31)
        return 2**31 - 1
