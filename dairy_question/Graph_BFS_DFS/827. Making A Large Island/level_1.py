class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        SEA = 0
        LAND = 1
        height = len(grid)
        width = len(grid[0])
        island_sizes = {0: 0}

        def mark_checked_island(row, col, island_number):
            queue = deque([(row, col)])
            island_size = 0
            while queue:
                h, w = queue.popleft()
                if not (0 <= h < height and 0 <= w < width):
                    continue
                if grid[h][w] != LAND:
                    continue
                grid[h][w] = island_number
                island_size += 1
                queue.append((h + 1, w))
                queue.append((h - 1, w))
                queue.append((h, w + 1))
                queue.append((h, w - 1))
            return island_size

        island_number = 2
        for row in range(height):
            for col in range(width):
                if grid[row][col] != LAND:
                    continue
                island_size = mark_checked_island(row, col, island_number)
                island_sizes[island_number] = island_size
                island_number += 1

        def get_neibors(row, col):
            neibors = set()
            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                h = row + dh
                w = col + dw
                if not (0 <= h < height and 0 <= w < width):
                    continue
                neibors.add(grid[h][w])
            return list(neibors)

        max_size = max(island_sizes.values())
        for row in range(height):
            for col in range(width):
                if grid[row][col] != SEA:
                    continue
                island_size = 1
                for i in get_neibors(row, col):
                    island_size += island_sizes[i]
                max_size = max(max_size, island_size)

        return max_size
