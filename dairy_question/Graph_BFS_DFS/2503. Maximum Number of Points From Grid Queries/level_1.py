# ブルートフォース(TLE)
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        height = len(grid)
        width = len(grid[0])

        @cache
        def search_under_k(k):
            num = 0
            seen = set()
            queue = deque([(0, 0)])
            while queue:
                row, col = queue.popleft()
                if (row, col) in seen:
                    continue
                seen.add((row, col))
                if grid[row][col] >= k:
                    continue
                num += 1
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_row = row + dx
                    next_col = col + dy
                    if not 0 <= next_row < height:
                        continue
                    if not 0 <= next_col < width:
                        continue
                    queue.append((next_row, next_col))
            return num

        num_under_k_list = []
        for query in queries:
            num_under_k_list.append(search_under_k(query))
        return num_under_k_list


# kを昇順に実行して前回の結果を再利用
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        height = len(grid)
        width = len(grid[0])
        seen = set()

        def search_under_k(k, position_heap):
            num = 0
            while position_heap and position_heap[0][0] < k:
                val, row, col = heappop(position_heap)
                if (row, col) in seen:
                    continue
                seen.add((row, col))
                num += 1
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_row = row + dx
                    next_col = col + dy
                    if not 0 <= next_row < height:
                        continue
                    if not 0 <= next_col < width:
                        continue
                    if (next_row, next_col) in seen:
                        continue
                    heappush(position_heap,
                             (grid[next_row][next_col], next_row, next_col))
            return num, position_heap

        count_under_k = {0: 0}
        position_heap = [(grid[0][0], 0, 0)]
        prev_k = 0
        for k in sorted(queries):
            if k in count_under_k:
                continue
            add_count, position_heap = search_under_k(k, position_heap)
            count_under_k[k] = count_under_k[prev_k] + add_count
            prev_k = k
        return [count_under_k[query] for query in queries]
