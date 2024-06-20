# 深さ優先探索
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        width = len(matrix[0])
        lengths = [[0] * width for _ in range(height)]

        @cache
        def calc_lengths(prev_val, h, w):
            if (not 0 <= h < height) or (not 0 <= w < width):
                return 0
            if matrix[h][w] <= prev_val:
                return 0
            max_length = 0
            max_length = max(max_length, calc_lengths(matrix[h][w], h + 1, w) + 1)
            max_length = max(max_length, calc_lengths(matrix[h][w], h - 1, w) + 1)
            max_length = max(max_length, calc_lengths(matrix[h][w], h, w + 1) + 1)
            max_length = max(max_length, calc_lengths(matrix[h][w], h, w - 1) + 1)
            lengths[h][w] = max_length
            return max_length

        for h in range(height):
            for w in range(width):
                if lengths[h][w]:
                    continue
                calc_lengths(-math.inf, h, w)

        max_length = 0
        for h in range(height):
            max_length = max(max_length, max(lengths[h]))
        return max_length
