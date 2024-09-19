# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND = "1"
        SEA = "0"
        height = len(grid)
        width = len(grid[0])
        seen = set()
        land_num = 0

        def mark_grid(row, col):
            queue = deque([(row, col)])
            while queue:
                h, w = queue.popleft()
                if not (0 <= h < height and 0 <= w < width):
                    continue
                if (h, w) in seen:
                    continue
                seen.add((h, w))
                if grid[h][w] == SEA:
                    continue
                queue.append((h + 1, w))
                queue.append((h - 1, w))
                queue.append((h, w + 1))
                queue.append((h, w - 1))

        for row in range(height):
            for col in range(width):
                if (row, col) in seen:
                    continue
                if grid[row][col] == SEA:
                    continue
                land_num += 1
                mark_grid(row, col)

        return land_num
