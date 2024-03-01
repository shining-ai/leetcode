# 深さ優先探索
# setではなく、grid_copyでチェック済みを管理するように修正
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        grid_copy = copy.deepcopy(grid)

        def mark_connected_island(h, w):
            if not (0 <= h < height) or not (0 <= w < width):
                return
            if grid_copy[h][w] == "0":
                return
            grid_copy[h][w] = "0"
            mark_connected_island(h + 1, w)
            mark_connected_island(h - 1, w)
            mark_connected_island(h, w + 1)
            mark_connected_island(h, w - 1)

        island_count = 0
        for h in range(height):
            for w in range(width):
                if grid_copy[h][w] == "0":
                    continue
                mark_connected_island(h, w)
                island_count += 1
        return island_count


# 幅優先探索
# setではなく、grid_copyでチェック済みを管理するように修正
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        grid_copy = copy.deepcopy(grid)
        queue = deque()
        island_count = 0

        def mark_connected_island(h, w):
            queue.append((h, w))
            while queue:
                row, col = queue.popleft()
                if not (0 <= row < height) or not (0 <= col < width):
                    continue
                if grid_copy[row][col] == "0":
                    continue
                grid_copy[row][col] = "0"
                queue.append((row + 1, col))
                queue.append((row - 1, col))
                queue.append((row, col + 1))
                queue.append((row, col - 1))

        for h in range(height):
            for w in range(width):
                if grid_copy[h][w] == "0":
                    continue
                island_count += 1
                mark_connected_island(h, w)

        return island_count


# UnionFind
# grid_copyでチェック済みを管理して、unite_treeを呼ぶ回数を減らした
class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [1] * n

    def find_root(self, x):
        while self.parent[x] != -1:
            x = self.parent[x]
        return x

    def unite_tree(self, node1, node2):
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
        grid_copy = copy.deepcopy(grid)

        def neibor_unite_tree(neibor_h, neibor_w, index):
            if not (0 <= neibor_h < height) or not (0 <= neibor_w < width):
                return
            if grid_copy[neibor_h][neibor_w] == "0":
                return
            neibor_index = width * neibor_h + neibor_w
            uf.unite_tree(index, neibor_index)

        for h in range(height):
            for w in range(width):
                if grid_copy[h][w] == "0":
                    continue
                grid_copy[h][w] = "0"
                index = width * h + w
                neibor_unite_tree(h + 1, w, index)
                neibor_unite_tree(h - 1, w, index)
                neibor_unite_tree(h, w + 1, index)
                neibor_unite_tree(h, w - 1, index)
        island_count = 0
        for h in range(height):
            for w in range(width):
                index = width * h + w
                if grid[h][w] == "1" and uf.is_root(index):
                    island_count += 1
        return island_count
