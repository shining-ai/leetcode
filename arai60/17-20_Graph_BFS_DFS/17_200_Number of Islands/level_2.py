# 深さ優先探索
# setではなく、marking_gridでチェック済みを管理するように修正
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        marking_grid = copy.deepcopy(grid)

        def mark_connected_island(h, w):
            if not ((0 <= h < height) and (0 <= w < width)):
                return
            if marking_grid[h][w] == "0":
                return
            marking_grid[h][w] = "0"
            mark_connected_island(h + 1, w)
            mark_connected_island(h - 1, w)
            mark_connected_island(h, w + 1)
            mark_connected_island(h, w - 1)

        island_count = 0
        for h in range(height):
            for w in range(width):
                if marking_grid[h][w] == "0":
                    continue
                mark_connected_island(h, w)
                island_count += 1
        return island_count


# 幅優先探索
# setではなく、marking_gridでチェック済みを管理するように修正
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        marking_grid = copy.deepcopy(grid)
        queue_land = deque()
        island_count = 0

        def mark_connected_island(h, w):
            queue_land.append((h, w))
            while queue_land:
                row, col = queue_land.popleft()
                if not ((0 <= row < height) and (0 <= col < width)):
                    continue
                if marking_grid[row][col] == "0":
                    continue
                marking_grid[row][col] = "0"
                queue_land.append((row + 1, col))
                queue_land.append((row - 1, col))
                queue_land.append((row, col + 1))
                queue_land.append((row, col - 1))

        for h in range(height):
            for w in range(width):
                if marking_grid[h][w] == "0":
                    continue
                island_count += 1
                mark_connected_island(h, w)

        return island_count


# UnionFind
# marking_gridでチェック済みを管理して、unite_treeを呼ぶ回数を減らした
class UnionFind:
    def __init__(self, node_num):
        self.parent = [-1] * node_num
        self.size = [1] * node_num

    def find_root(self, node):
        while not self.is_root(node):
            node = self.parent[node]
        return node

    def union_tree(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if root1 == root2:
            return
        # union by size：大きい木を親にすると計算量がO(logN)になる。
        if self.size[root1] < self.size[root2]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]

    def is_root(self, node):
        return self.parent[node] == -1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        uf = UnionFind(height * width)
        marking_grid = copy.deepcopy(grid)

        def make_index(h, w):
            return width * h + w

        def unite_next_tree(h, w):
            index = make_index(h, w)
            next_pos = [(h + 1, w), (h - 1, w), (h, w + 1), (h, w - 1)]
            for next_h, next_w in next_pos:
                if not ((0 <= next_h < height) and (0 <= next_w < width)):
                    continue
                if marking_grid[next_h][next_w] == "0":
                    continue
                next_index = make_index(next_h, next_w)
                uf.union_tree(index, next_index)

        for h in range(height):
            for w in range(width):
                if marking_grid[h][w] == "0":
                    continue
                marking_grid[h][w] = "0"
                unite_next_tree(h, w)
        island_count = 0
        for h in range(height):
            for w in range(width):
                index = make_index(h, w)
                if grid[h][w] == "1" and uf.is_root(index):
                    island_count += 1
        return island_count
