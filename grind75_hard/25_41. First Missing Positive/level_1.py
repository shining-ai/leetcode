class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        success_board = []

        def can_set(current, col):
            if col in current:
                return False
            row = len(current)
            for i_row, i_col in enumerate(current):
                if i_col + abs(row - i_row) == col:
                    return False
                if i_col - abs(row - i_row) == col:
                    return False
            return True

        def helper(current):
            if n == len(current):
                success_board.append(current[:])
                return
            for col in range(n):
                if not can_set(current, col):
                    continue
                current.append(col)
                helper(current)
                current.pop()

        helper([])
        boards = []
        for queen in success_board:
            board = []
            for row, col in enumerate(queen):
                row_condition = ""
                for i in range(n):
                    if i == col:
                        row_condition += "Q"
                    else:
                        row_condition += "."
                board.append(row_condition)
            boards.append(board)

        return boards
