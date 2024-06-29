# 2DP
# 配る形式に変更
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        num_paths = [[0] * width for _ in range(height)]
        if obstacleGrid[0][0] == 0:
            num_paths[0][0] = 1
        for row in range(height):
            for column in range(width):
                if obstacleGrid[row][column] == 1:
                    num_paths[row][column] = 0
                    continue
                if row + 1 < height:
                    num_paths[row + 1][column] += num_paths[row][column]
                if column + 1 < width:
                    num_paths[row][column + 1] += num_paths[row][column]

        return num_paths[-1][-1]


# 1DP
# 配る形式に変更
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        num_paths = [0] * width
        if obstacleGrid[0][0] == 0:
            num_paths[0] = 1
        for row in range(height):
            for column in range(width):
                if obstacleGrid[row][column] == 1:
                    num_paths[column] = 0
                    continue
                if column + 1 < width:
                    num_paths[column + 1] += num_paths[column]
        return num_paths[-1]
