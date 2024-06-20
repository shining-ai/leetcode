# トポロジカルソート
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        width = len(matrix[0])
        level = 0
        inDegree = [[0] * width for _ in range(height)]
        direction = ((0, -1), (-1, 0), (0, 1), (1, 0))

        for row in range(height):
            for col in range(width):
                for dx, dy in direction:
                    x, y = row + dx, col + dy
                    if not (0 <= x < height) or not (0 <= y < width):
                        continue
                    if matrix[x][y] <= matrix[row][col]:
                        continue
                    inDegree[x][y] += 1

        queue = deque()
        for row in range(height):
            for col in range(width):
                if inDegree[row][col] == 0:
                    queue.append((row, col))

        while queue:
            next_queue = deque()
            while queue:
                row, col = queue.popleft()
                for dx, dy in direction:
                    x, y = row + dx, col + dy
                    if not (0 <= x < height) or not (0 <= y < width):
                        continue
                    if matrix[x][y] <= matrix[row][col]:
                        continue
                    inDegree[x][y] -= 1
                    if inDegree[x][y] == 0:
                        next_queue.append((x, y))  # HASN'T VISITED THAT CELL YET
            queue = next_queue
            level += 1

        return level
