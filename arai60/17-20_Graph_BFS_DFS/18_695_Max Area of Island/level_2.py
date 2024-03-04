# 深さ優先探索
# 関数名を変更
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        seen = set()

        def measure_unsurveyed_island_size(h, w):
            if not ((0 <= h < height) and (0 <= w < width)):
                return 0
            if grid[h][w] == 0:
                return 0
            if (h, w) in seen:
                return 0
            seen.add((h, w))
            island_size = 1
            island_size += measure_unsurveyed_island_size(h + 1, w)
            island_size += measure_unsurveyed_island_size(h - 1, w)
            island_size += measure_unsurveyed_island_size(h, w + 1)
            island_size += measure_unsurveyed_island_size(h, w - 1)
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
                if not ((0 <= row < height) and (0 <= col < width)):
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
        seen = set()

        def make_index(h, w):
            return h * width + w

        def unite_next_tree(h, w):
            index = make_index(h, w)
            next_pos = [(h + 1, w), (h - 1, w), (h, w + 1), (h, w - 1)]
            for next_h, next_w in next_pos:
                if not ((0 <= next_h < height) and (0 <= next_w < width)):
                    continue
                if grid[next_h][next_w] == 0:
                    continue
                if (next_h, next_w) in seen:
                    continue
                next_index = make_index(next_h, next_w)
                uf.union_tree(index, next_index)

        for h in range(height):
            for w in range(width):
                if grid[h][w] == 0:
                    continue
                seen.add((h, w))
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
