# 経路圧縮を実装
class UnionFind:
    def __init__(self, node_num):
        self.parent = [-1] * node_num
        self.size = [1] * node_num

    def is_root(self, node_id):
        return self.parent[node_id] == -1

    def find_root(self, node_id):
        root = node_id
        while not self.is_root(root):
            root = self.parent[root]
        while not self.is_root(node_id):
            temp = node_id
            node_id = self.parent[node_id]
            self.parent[temp] = root
        return root

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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for node1, node2 in edges:
            uf.union_tree(node1, node2)
        unique = 0
        for i in range(n):
            if uf.is_root(i):
                unique += 1
        return unique


# 経路圧縮を再帰で実装
class UnionFind:
    def __init__(self, node_num):
        self.parent = [-1] * node_num
        self.size = [1] * node_num

    def is_root(self, node_id):
        return self.parent[node_id] == -1

    def find_root(self, node_id):
        if self.is_root(node_id):
            return node_id
        root = self.find_root(self.parent[node_id])
        self.parent[node_id] = root
        return root

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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for node1, node2 in edges:
            uf.union_tree(node1, node2)
        unique = 0
        for i in range(n):
            if uf.is_root(i):
                unique += 1
        return unique
