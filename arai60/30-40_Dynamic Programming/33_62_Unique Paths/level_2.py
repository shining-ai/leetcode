# 数学の組み合わせの問題として計算
# math.comb()を使う
# math.combの第2引数は特別な意図はない(num_downとnum_rightのどちらを使っても変わらない?)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_down = m - 1
        num_right = n - 1
        return math.comb(num_down + num_right, num_down)


# 各マスに到達する全ての組み合わせを計算
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_unique_path = [[1] * n for _ in range(m)]
        for col in range(1, m):
            for row in range(1, n):
                num_unique_path[col][row] = (
                    num_unique_path[col - 1][row]
                    + num_unique_path[col][row - 1]
                )
        return num_unique_path[m - 1][n - 1]
