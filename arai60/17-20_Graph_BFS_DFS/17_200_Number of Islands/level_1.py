# O(M * N) time complexity
# O(M * N) space complexity
def solve_1(grid):
    row_num = len(grid)
    collumn_num = len(grid[0])

    def dfs(grid, row, collumn):
        if row < 0 or collumn < 0 or row >= row_num or collumn >= collumn_num:
            return

        if grid[row][collumn] == "0":
            return

        grid[row][collumn] = "0"
        dfs(grid, row - 1, collumn)
        dfs(grid, row + 1, collumn)
        dfs(grid, row, collumn - 1)
        dfs(grid, row, collumn + 1)

    ans = 0

    for i in range(row_num):
        for j in range(collumn_num):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                ans += 1

    return ans


from collections import deque


# O(M * N) time complexity
# O(min(M , N)) space complexity
def solve_2(grid):
    queue = deque([])
    row_num = len(grid)
    collumn_num = len(grid[0])
    ans = 0

    for i_row in range(row_num):
        for j_collumn in range(collumn_num):
            if grid[i_row][j_collumn] == "1":
                queue.append((i_row, j_collumn))
                ans += 1

                while queue:
                    i, j = queue.popleft()

                    if i < 0 or j < 0 or i >= row_num or j >= collumn_num:
                        continue

                    if grid[i][j] == "0":
                        continue

                    grid[i][j] = "0"
                    queue.append((i - 1, j))
                    queue.append((i + 1, j))
                    queue.append((i, j - 1))
                    queue.append((i, j + 1))

    return ans


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    print(solve_1(grid))
    print(solve_2(grid))
