# UnionFind
# root一覧を作らずカウントだけするように修正
class UnionFind:
    def __init__(self, node_num):
        self.parent = [-1] * node_num
        self.size = [1] * node_num

    def is_root(self, node_id):
        return self.parent[node_id] == -1

    def find_root(self, node_id):
        while not self.is_root(node_id):
            node_id = self.parent[node_id]
        return node_id

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
        for i in range(n):
            if uf.is_root(i):
                root_num += 1
        return root_num


# DFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for node_id in range(n)]
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        seen = set()

        def mark_connected_node(node_id):
            if node_id in seen:
                return
            seen.add(node_id)
            next_nodes = graph[node_id]
            for next_node in next_nodes:
                mark_connected_node(next_node)

        count = 0
        for node_id in range(n):
            if node_id in seen:
                continue
            count += 1
            mark_connected_node(node_id)
        return count


# BFS
# キューからスタックに変更
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for node_id in range(n)]
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        def mark_connected_node(start_node):
            stack = [start_node]
            while stack:
                node_id = stack.pop()
                seen.add(node_id)
                next_nodes = graph[node_id]
                for next_node in next_nodes:
                    if next_node in seen:
                        continue
                    stack.append(next_node)

        seen = set()
        count = 0
        for i in range(n):
            if i in seen:
                continue
            count += 1
            mark_connected_node(i)
        return count
