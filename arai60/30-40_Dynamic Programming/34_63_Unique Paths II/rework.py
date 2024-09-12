# 貰うDP(2DP)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        patterns = [[0] * width for _ in range(height)]
        for row in range(height):
            if obstacleGrid[row][0] == 1:
                break
            patterns[row][0] = 1
        for col in range(width):
            if obstacleGrid[0][col] == 1:
                break
            patterns[0][col] = 1
        for row in range(1, height):
            for col in range(1, width):
                if obstacleGrid[row][col] == 1:
                    patterns[row][col] = 0
                    continue
                patterns[row][col] = patterns[row - 1][col] + patterns[row][col - 1]
        return patterns[-1][-1]


# 配るDP(2DP)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        patterns = [[0] * width for _ in range(height)]
        if obstacleGrid[0][0] == 1:
            return 0
        patterns[0][0] = 1
        for row in range(height):
            for col in range(width):
                if obstacleGrid[row][col] == 1:
                    patterns[row][col] = 0
                    continue
                if row + 1 < height:
                    patterns[row + 1][col] += patterns[row][col]
                if col + 1 < width:
                    patterns[row][col + 1] += patterns[row][col]
        return patterns[-1][-1]
