# level_1をループで表現
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate_power(base, exp):
            power_result = 1
            while 0 < exp:
                if exp % 2 == 1:
                    power_result *= base
                    exp -= 1
                base *= base
                exp = exp // 2
            return power_result

        if n < 0:
            return 1 / calculate_power(x, -n)
        return calculate_power(x, n)


# Pythonの組み込み関数pow()を参考に実装
# https://github.com/python/cpython/blob/109fc2792a490ee5cd8a423e17d415fbdedec5c8/Objects/longobject.c#L4244-L4447
# https://qiita.com/AkariLuminous/items/ab3f382643e92122f8ef
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        def calculate_power(base, exp):
            current_bit = 1 << exp.bit_length() - 1
            power_result = 1
            while current_bit:
                power_result *= power_result
                if exp & current_bit:
                    power_result *= base
                current_bit >>= 1
            return power_result

        if n < 0:
            return 1 / calculate_power(x, -n)
        return calculate_power(x, n)
