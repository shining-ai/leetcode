# 数学の組み合わせの問題として計算
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_down = m - 1
        num_right = n - 1

        def combination(n, k):
            res = 1
            for i in range(n, k, -1):
                res *= i
            for i in range(n - k, 1, -1):
                res //= i
            return res

        return combination(num_down + num_right, max(num_down, num_right))
