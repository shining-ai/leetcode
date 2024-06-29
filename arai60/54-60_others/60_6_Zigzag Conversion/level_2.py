# 何行目になるかは規則性があるので計算で求められる
# 2*n-2個周期で行が繰り返される
# 0     6
# 1   5 7
# 2 4   8
# 3
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        cycle = 2 * numRows - 2
        for i in range(len(s)):
            pos = i % (cycle)
            if pos < numRows:  # 下りのとき
                num_row = pos
            else:  # 上りのとき
                # [最下行] - [折り返して何個目か]
                # (numRows - 1) - (pos - (numRows - 1))
                num_row = 2 * numRows - pos - 2
            rows[num_row].append(s[i])
        marged_all_rows = []
        for row in rows:
            marged_all_rows.extend(row)
        zigzag_string = "".join(marged_all_rows)
        return zigzag_string
