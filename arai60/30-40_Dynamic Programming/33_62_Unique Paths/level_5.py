# 空間計算量 O(m)
# 1DPで解く
# n, mの小さい方をメモリに格納すればO(min(n, m))にできそう
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            self.uniquePaths(n, m)
        num_unique_path = [1] * m
        for col in range(1, n):
            for row in range(1, m):
                num_unique_path[row] += num_unique_path[row - 1]
        return num_unique_path[-1]
