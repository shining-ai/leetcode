# 2DP(配る形式)
# obstacleGrid[-1][-1] == 1のチェックを最初に追加
# 変数の初期化をfor文の中に移動
# そもそも1回のループで2つの値を更新するのは分かり辛いかも
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        OBSTACLE = 1
        SPACE = 0
        if obstacleGrid[-1][-1] == OBSTACLE:
            return 0
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        num_paths = [[0] * width for _ in range(height)]
        for row in range(height):
            for column in range(width):
                if row == 0 and column == 0:
                    if obstacleGrid[0][0] == SPACE:
                        num_paths[0][0] = 1
                    continue
                if obstacleGrid[row][column] == OBSTACLE:
                    continue
                if row + 1 < height:
                    num_paths[row + 1][column] += num_paths[row][column]
                if column + 1 < width:
                    num_paths[row][column + 1] += num_paths[row][column]
        return num_paths[-1][-1]


# 2DP(貰う形式)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        OBSTACLE = 1
        SPACE = 0
        if obstacleGrid[-1][-1] == OBSTACLE:
            return 0
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        num_paths = [[0] * width for _ in range(height)]
        for row in range(height):
            for column in range(width):
                if row == 0 and column == 0:
                    if obstacleGrid[0][0] == SPACE:
                        num_paths[0][0] = 1
                    continue
                if obstacleGrid[row][column] == 1:
                    continue
                if 0 <= row - 1:
                    num_paths[row][column] += num_paths[row - 1][column]
                if 0 <= column - 1:
                    num_paths[row][column] += num_paths[row][column - 1]
        return num_paths[-1][-1]
