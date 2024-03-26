class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_unique_path = [[1] * n for _ in range(m)]
        for col in range(1, m):
            for row in range(1, n):
                num_unique_path[col][row] = num_unique_path[col-1][row] + num_unique_path[col][row-1]
        return num_unique_path[m-1][n-1]
