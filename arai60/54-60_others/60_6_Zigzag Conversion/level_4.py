class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        rows_index = 0
        direction = 1
        for c in s:
            rows[rows_index].append(c)
            if rows_index == 0:
                direction = 1
            if rows_index == numRows - 1:
                direction = -1
            rows_index += direction
        return "".join(c for row in rows for c in row)
