# pythonの演算子を使用
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n


# 単純なブルートフォース(TLE)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        power_result = 1
        if 0 < n:
            for _ in range(n):
                power_result *= x
        if n < 0:
            for _ in range(-n):
                power_result /= x
        return power_result


# Binary Exponentiation
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate_power(x, n):
            if n == 0:
                return 1
            if n % 2 == 1:
                return x * calculate_power(x * x, (n - 1) // 2)
            return calculate_power(x * x, n // 2)

        if n < 0:
            return 1 / calculate_power(x, -n)
        return calculate_power(x, n)
