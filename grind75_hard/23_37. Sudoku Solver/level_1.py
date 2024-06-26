class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        subgrid_side = 3
        n = len(board)
        row_digits = [set() for _ in range(n)]
        col_digits = [set() for _ in range(n)]
        box_digits = [set() for _ in range((n // 3) ** 2)]
        complete = False

        # 初期状態での数字を記録
        for row in range(n):
            for col in range(n):
                if board[row][col] == ".":
                    continue
                digit = int(board[row][col])
                row_digits[row].add(digit)
                col_digits[col].add(digit)
                box_digits[row // 3 * 3 + col // 3].add(digit)

        def can_set(row, col, digit):
            if digit in row_digits[row]:
                return False
            if digit in col_digits[col]:
                return False
            if (
                digit
                in box_digits[
                    subgrid_side * (row // subgrid_side) + (col // subgrid_side)
                ]
            ):
                return False
            return True

        def set_digit(row, col, digit):
            nonlocal complete
            row_digits[row].add(digit)
            col_digits[col].add(digit)
            box_digits[
                subgrid_side * (row // subgrid_side) + (col // subgrid_side)
            ].add(digit)
            board[row][col] = str(digit)
            if row == n - 1 and col == n - 1:
                complete = True

        def remove_digit(row, col, digit):
            row_digits[row].discard(digit)
            col_digits[col].discard(digit)
            box_digits[
                subgrid_side * (row // subgrid_side) + (col // subgrid_side)
            ].discard(digit)
            board[row][col] = "."

        def helper_solve(row, col):
            nonlocal complete

            if board[row][col] == ".":
                for i in range(1, n + 1):
                    if not can_set(row, col, i):
                        continue

                    set_digit(row, col, i)
                    if complete:
                        return
                    if col < n - 1:
                        helper_solve(row, col + 1)
                    else:
                        helper_solve(row + 1, 0)
                    if complete:
                        return

                    remove_digit(row, col, i)
            else:
                if row == n - 1 and col == n - 1:
                    complete = True
                    return
                if col < n - 1:
                    helper_solve(row, col + 1)
                else:
                    helper_solve(row + 1, 0)
                return

        helper_solve(0, 0)
        return board
