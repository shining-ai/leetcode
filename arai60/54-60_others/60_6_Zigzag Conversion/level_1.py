# 各行の文字列をリストに格納して、最後に結合する。
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        num_row = 0
        direction = 1
        for c in s:
            rows[num_row].append(c)
            if num_row == 0:  # 0行目で折り返し
                direction = 1
            if num_row == numRows - 1:  # 最終行で折り返し
                direction = -1
            num_row += direction
        merged_all_rows = []
        for row in rows:
            merged_all_rows.extend(row)
        zigzag_string = "".join(merged_all_rows)
        return zigzag_string
