class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        seen = set()

        def measure_island_size(h, w):
            if not ((0 <= h < height) and (0 <= w < width)):
                return 0
            if grid[h][w] == 0:
                return 0
            if (h, w) in seen:
                return 0
            seen.add((h, w))
            island_size = 1
            island_size += measure_island_size(h + 1, w)
            island_size += measure_island_size(h - 1, w)
            island_size += measure_island_size(h, w + 1)
            island_size += measure_island_size(h, w - 1)
            return island_size

        max_island_size = 0
        for h in range(height):
            for w in range(width):
                if (h, w) in seen:
                    continue
                if grid[h][w] == 0:
                    continue
                island_size = measure_island_size(h, w)
                max_island_size = max(max_island_size, island_size)
        return max_island_size
