# O(m*n) time complexity
# O(m*n) space complexity
def solve_1(grid):
    row_num = len(grid)
    collumn_num = len(grid[0])
    ans = 0

    def dfs(grid, row, collumn):
        island_size = 0

        if row < 0 or collumn < 0 or row >= row_num or collumn >= collumn_num:
            return 0

        if grid[row][collumn] == 0:
            return 0

        grid[row][collumn] = 0
        island_size += dfs(grid, row - 1, collumn)
        island_size += dfs(grid, row + 1, collumn)
        island_size += dfs(grid, row, collumn - 1)
        island_size += dfs(grid, row, collumn + 1)
        return island_size + 1

    for i in range(row_num):
        for j in range(collumn_num):
            if grid[i][j] == 1:
                island_size = dfs(grid, i, j)
                ans = max(ans, island_size)

    return ans


def solve_2(grid):
    seen = set()
    ans = 0
    for i, i_row in enumerate(grid):
        for j, j_collumn in enumerate(i_row):
            if j_collumn and (i, j) not in seen:
                shape = 0
                stack = [(i, j)]
                seen.add((i, j))
                while stack:
                    i, j = stack.pop()
                    shape += 1
                    for i_new, j_new in (
                        (i + 1, j),
                        (i - 1, j),
                        (i, j + 1),
                        (i, j - 1),
                    ):
                        if (
                            0 <= i_new < len(grid)
                            and 0 <= j_new < len(grid[0])
                            and grid[i_new][j_new]
                            and (i_new, j_new) not in seen
                        ):
                            stack.append((i_new, j_new))
                            seen.add((i_new, j_new))
                ans = max(ans, shape)
    return ans


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    print(solve_1(grid))
