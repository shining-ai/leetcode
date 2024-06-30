class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate_power(base, exp):
            if exp == 0:
                return 1
            if exp % 2 == 1:
                return base * calculate_power(base * base, (exp - 1) // 2)
            return calculate_power(base * base, exp // 2)

        if n < 0:
            return 1 / calculate_power(x, -n)
        return calculate_power(x, n)
