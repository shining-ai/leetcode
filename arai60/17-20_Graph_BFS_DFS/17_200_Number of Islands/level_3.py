# 深さ優先探索
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        copy_grid = copy.deepcopy(grid)

        def mark_connected_land(h, w):
            if not (0 <= h < height) or not (0 <= w < width):
                return
            if copy_grid[h][w] == "0":
                return
            copy_grid[h][w] = "0"
            mark_connected_land(h + 1, w)
            mark_connected_land(h - 1, w)
            mark_connected_land(h, w + 1)
            mark_connected_land(h, w - 1)

        island_count = 0
        for h in range(height):
            for w in range(width):
                if copy_grid[h][w] == "0":
                    continue
                island_count += 1
                mark_connected_land(h, w)

        return island_count
