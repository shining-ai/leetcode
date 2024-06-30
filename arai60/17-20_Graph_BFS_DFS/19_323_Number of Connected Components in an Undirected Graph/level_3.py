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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for node1, node2 in edges:
            uf.union_tree(node1, node2)
        root_num = 0
        for node in range(n):
            if uf.is_root(node):
                root_num += 1
        return root_num


# 別途ユニークなグループを数えるのでもいいですが、unionした回数を覚えておいて総数から引いても良いかなと思います。
# 例）3個のコンポーネントがあり、1回繋げると、3-1の2個のコンポーネントが残る。
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
            return False
        if self.size[root1] < self.size[root2]:
            small, big = root1, root2
        else:
            small, big = root2, root1
        self.parent[small] = big
        self.size[big] += self.size[small]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        union_num = 0
        for node1, node2 in edges:
            if uf.union_tree(node1, node2):
                union_num += 1
        root_num = n - union_num
        return root_num
