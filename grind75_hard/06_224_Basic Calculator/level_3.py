class Solution:
    def calculate(self, s: str) -> int:
        def helper_calculate(index):
            num = 0
            sign = 1
            result = 0
            while index < len(s):
                if s[index].isdigit():
                    num = 10 * num + int(s[index])
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
                    return result, index
                if s[index] == "(":
                    result_in_brackets, index = helper_calculate(index + 1)
                    result += result_in_brackets * sign
                index += 1
            result += num * sign
            return result

        return helper_calculate(0)
