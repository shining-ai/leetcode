# 深さ優先探索
# 関数名を変更
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        seen = set()

        def measure_unsurveyed_island_size(row, col):
            if not ((0 <= row < len(grid)) and (0 <= col < len(grid[row]))):
                return 0
            if grid[row][col] == 0:
                return 0
            if (row, col) in seen:
                return 0
            seen.add((row, col))
            island_size = 1
            island_size += measure_unsurveyed_island_size(row + 1, col)
            island_size += measure_unsurveyed_island_size(row - 1, col)
            island_size += measure_unsurveyed_island_size(row, col + 1)
            island_size += measure_unsurveyed_island_size(row, col - 1)
            return island_size

        max_island_size = 0
        for h in range(height):
            for w in range(width):
                island_size = measure_unsurveyed_island_size(h, w)
                max_island_size = max(max_island_size, island_size)
        return max_island_size


# 幅優先探索
# 島のサイズを計測する部分を関数化
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        seen = set()
        queue_island = deque()

        def measure_unsurveyed_island_size(h, w):
            queue_island.append((h, w))
            island_size = 0
            while queue_island:
                row, col = queue_island.popleft()
                if not (
                    (0 <= row < len(grid)) and (0 <= col < len(grid[row]))
                ):
                    continue
                if grid[row][col] == 0:
                    continue
                if (row, col) in seen:
                    continue
                seen.add((row, col))
                island_size += 1
                queue_island.append((row + 1, col))
                queue_island.append((row - 1, col))
                queue_island.append((row, col + 1))
                queue_island.append((row, col - 1))
            return island_size

        max_island_size = 0
        for h in range(height):
            for w in range(width):
                island_size = measure_unsurveyed_island_size(h, w)
                max_island_size = max(max_island_size, island_size)
        return max_island_size


# UnionFind
# 関数名を修正
# 変数island_sizeを作成
# 右と下方向だけ確認して結合するように修正
# seenは不要のため削除
class UnionFind:
    def __init__(self, node_num):
        self.parent = [-1] * node_num
        self.size = [1] * node_num

    def is_root(self, node):
        return self.parent[node] == -1

    def find_root(self, node):
        while not self.is_root(node):
            node = self.parent[node]
        return node

    def union_tree(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if root1 == root2:
            return
        if self.size[root1] < self.size[root2]:
            small, big = root1, root2
        else:
            small, big = root2, root1
        self.parent[small] = big
        self.size[big] += self.size[small]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        uf = UnionFind(height * width)

        def make_index(row, col):
            return row * width + col

        def unite_next_tree(row, col):
            index = make_index(row, col)
            next_pos = [(row + 1, col), (row, col + 1)]
            for next_row, next_col in next_pos:
                if not (
                    (next_row < len(grid)) and (next_col < len(grid[next_row]))
                ):
                    continue
                if grid[next_row][next_col] == 0:
                    continue
                next_index = make_index(next_row, next_col)
                uf.union_tree(index, next_index)

        for h in range(height):
            for w in range(width):
                if grid[h][w] == 0:
                    continue
                unite_next_tree(h, w)
        max_island_size = 0
        for h in range(height):
            for w in range(width):
                if grid[h][w] == 0:
                    continue
                index = make_index(h, w)
                island_size = uf.size[index]
                max_island_size = max(max_island_size, island_size)
        return max_island_size
