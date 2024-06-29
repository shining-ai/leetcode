# -(2**31)でオーバーフローしていたので修正
# オーバーフローの判定を%演算子を使うように修正
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        def skip_space(index):
            while index < len(s) and s[index].isspace():
                index += 1
            return index

        def parse_sign(index):
            sign = 1
            if index < len(s) and (s[index] == "-" or s[index] == "+"):
                if s[index] == "-":
                    sign = -1
                return index + 1, sign
            return index, sign

        def is_overflow(current_value, sign, next_digit):
            if sign == 1:
                if current_value > INT_MAX // 10:
                    return True
                if (
                    current_value == INT_MAX // 10
                    and next_digit >= INT_MAX % 10
                ):
                    return True
            if sign == -1:
                if current_value < (INT_MIN // 10) + 1:
                    return True
                if current_value == (
                    INT_MIN // 10
                ) + 1 and next_digit >= 10 - (INT_MIN % 10):
                    return True
            return False

        def convert_to_int(index, sign):
            value = 0
            while index < len(s) and "0" <= s[index] <= "9":
                digit = ord(s[index]) - ord("0")
                if is_overflow(value, sign, digit):
                    if sign == 1:
                        return INT_MAX
                    else:
                        return INT_MIN
                value *= 10
                value += digit * sign
                index += 1
            return value

        index = 0
        index = skip_space(index)
        index, sign = parse_sign(index)
        value = convert_to_int(index, sign)
        return value
