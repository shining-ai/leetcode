# UnionFind
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
        for edge in edges:
            uf.union_tree(edge[0], edge[1])
        unique_root = set()
        for i in range(n):
            unique_root.add(uf.find_root(i))
        return len(unique_root)


# DFS
# 解答を見て作成
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = [set() for node in range(n)]
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            components[node1].add(node2)
            components[node2].add(node1)
        seen = set()

        def mark_connected_node(node):
            seen.add(node)
            for next_node in components[node]:
                if next_node in seen:
                    continue
                mark_connected_node(next_node)

        count = 0
        for node in range(n):
            if node in seen:
                continue
            count += 1
            mark_connected_node(node)
        return count


# BFS
# 解答を見て作成
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = [set() for node in range(n)]
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            components[node1].add(node2)
            components[node2].add(node1)
        seen = set()
        queue = deque()
        count = 0
        for i in range(n):
            if i in seen:
                continue
            count += 1
            queue.append(i)
            while queue:
                node = queue.popleft()
                seen.add(node)
                for next_node in components[node]:
                    if next_node in seen:
                        continue
                    queue.append(next_node)

        return count
