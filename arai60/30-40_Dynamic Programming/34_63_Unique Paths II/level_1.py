# 2DP
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        num_paths = [[0] * width for _ in range(height)]
        for row in range(height):
            if obstacleGrid[row][0] == 1:
                break
            num_paths[row][0] = 1
        for column in range(width):
            if obstacleGrid[0][column] == 1:
                break
            num_paths[0][column] = 1
        for row in range(1, height):
            for column in range(1, width):
                if obstacleGrid[row][column] == 1:
                    continue
                num_paths[row][column] = (
                    num_paths[row - 1][column] + num_paths[row][column - 1]
                )

        return num_paths[-1][-1]


# 1DP
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        num_paths = [0] * width
        for column in range(width):
            if obstacleGrid[0][column] == 1:
                break
            num_paths[column] = 1
        for row in range(1, height):
            if obstacleGrid[row][0] == 1:
                num_paths[0] = 0
            for column in range(1, width):
                if obstacleGrid[row][column] == 1:
                    num_paths[column] = 0
                else:
                    num_paths[column] += num_paths[column - 1]
        return num_paths[-1]
