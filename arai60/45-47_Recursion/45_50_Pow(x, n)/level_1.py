class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n


# 単純なブルートフォース(TLE)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n > 0:
            for i in range(n):
                ans *= x
            return ans
        else:
            for i in range(-n):
                ans /= x
            return ans

# 解答を見た
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binary_exp(x, n):
            if n == 0:
                return 1
            if n % 2 == 1:
                return x * binary_exp(x * x, (n - 1) // 2)
            assert n % 2 == 0
            return binary_exp(x * x, n // 2)

        if n < 0:
            ans = 1 / binary_exp(x, -n)
        else:
            ans = binary_exp(x, n)
        return ans
