# 数学的な解法
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def combinations(n, k):
            res = 1
            for i in range(n - k + 1, n + 1):
                res *= i
            for i in range(1, k + 1):
                res //= i
            return res

        return combinations(m + n - 2, n - 1)


# 配るDP(2DP)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        patterns = [[0] * n for _ in range(m)]
        patterns[0][0] = 1
        for row in range(m):
            for col in range(n):
                if col + 1 < n:
                    patterns[row][col + 1] += patterns[row][col]
                if row + 1 < m:
                    patterns[row + 1][col] += patterns[row][col]
        return patterns[-1][-1]


# 貰うDP(2DP)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1
        for row in range(m):
            for col in range(n):
                if 0 <= row - 1 < m:
                    grid[row][col] += grid[row - 1][col]
                if 0 <= col - 1 < n:
                    grid[row][col] += grid[row][col - 1]
        return grid[-1][-1]
