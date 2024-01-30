def solve_1(obstacleGrid):
    row_num = len(obstacleGrid)
    col_num = len(obstacleGrid[0])

    route_num = [[0] * (col_num + 1) for _ in range(row_num + 1)]
    if obstacleGrid[0][0] == 0:
        route_num[1][1] = 1

    for i_col in range(1, col_num + 1):
        for i_row in range(1, row_num + 1):
            if obstacleGrid[i_row - 1][i_col - 1] == 1:
                continue

            route_num[i_row][i_col] += (
                route_num[i_row - 1][i_col] + route_num[i_row][i_col - 1]
            )

    return route_num[-1][-1]


if __name__ == "__main__":
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    print(solve_1(obstacleGrid))
