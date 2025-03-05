class Solution:
    def coloredCells(self, n: int) -> int:

        num_cell = 1
        for i in range(n):
            num_cell += 4 * i
        return num_cell


class Solution:
    def coloredCells(self, n: int) -> int:
        # 1, 2, 3, 4
        # 1, 4, 9, 16
        # 0, 1, 4, 9
        return n ** 2 + (n-1) ** 2
