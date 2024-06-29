# 各処理を関数化
# オーバーフローの判定をint範囲内に収めるように変更
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
                if current_value == INT_MAX // 10 and next_digit >= 7:
                    return True
            if sign == -1:
                if current_value > INT_MAX // 10:
                    return True
                if current_value == INT_MAX // 10 and next_digit >= 8:
                    return True
            return False

        def convert_to_int(index, sign):
            value_abs = 0
            while index < len(s) and "0" <= s[index] <= "9":
                digit = ord(s[index]) - ord("0")
                if is_overflow(value_abs, sign, digit):
                    if sign == 1:
                        return INT_MAX
                    else:
                        return INT_MIN
                value_abs *= 10
                value_abs += digit
                index += 1
            return value_abs * sign

        index = 0
        index = skip_space(index)
        index, sign = parse_sign(index)
        value = convert_to_int(index, sign)
        return value


# for文を使う
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        value = 0
        sign = 1
        finish_space = False
        finish_sign = False
        for c in s:
            if not finish_space and c.isspace():
                continue
            finish_space = True
            if not finish_sign and (c == "-" or c == "+"):
                if c == "-":
                    sign *= -1
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
