# -(2**31)でオーバーフローしていたので修正
# オーバーフローの判定を%演算子を使うように修正
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 0
        for _ in range(31):
            INT_MAX = (INT_MAX << 1) + 1
        INT_MIN = -(2**31)

        def skip_space(s):
            for index, c in enumerate(s):
                if not c.isspace():
                    return s[index:]
            return []

        def parse_sign_and_consume_index(s):
            sign = 1
            if not s:
                return [], sign
            if s[0] == "-" or s[0] == "+":
                if s[0] == "-":
                    sign = -1
                return s[1:], sign
            return s, sign

        def is_overflow(current_value, sign, next_digit):
            if sign == 1:
                if current_value > INT_MAX // 10:
                    return True
                if current_value == INT_MAX // 10 and next_digit > INT_MAX % 10:
                    return True
            if sign == -1:
                if current_value < (INT_MIN // 10) + 1:
                    return True
                if current_value == (INT_MIN // 10) + 1 and next_digit >= 10 - (
                    INT_MIN % 10
                ):
                    return True
            return False

        def convert_to_int(s, sign):
            value = 0
            for c in s:
                if not "0" <= c <= "9":
                    break
                digit = ord(c) - ord("0")
                if is_overflow(value, sign, digit):
                    if sign == 1:
                        return INT_MAX
                    else:
                        return INT_MIN
                value *= 10
                value += digit * sign
            return value

        remain_s = skip_space(s)
        remain_s, sign = parse_sign_and_consume_index(remain_s)
        value = convert_to_int(remain_s, sign)
        return value
