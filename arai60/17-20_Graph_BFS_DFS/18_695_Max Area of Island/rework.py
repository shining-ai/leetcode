# BFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LAND = 1
        SEA = 0
        height = len(grid)
        width = len(grid[0])
        seen = set()

        def is_land(row, col):
            if not (0 <= row < height and 0 <= col < width):
                return False
            return grid[row][col] == LAND

        def count_land_size(row, col):
            island_size = 0
            queue_island = deque([(row, col)])
            while queue_island:
                h, w = queue_island.popleft()
                if (h, w) in seen:
                    continue
                seen.add((h, w))
                island_size += 1
                for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if is_land(h + dh, w + dw):
                        queue_island.append((h + dh, w + dw))
            return island_size

        max_island = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == SEA:
                    continue
                island_size = count_land_size(row, col)
                max_island = max(max_island, island_size)
        return max_island
