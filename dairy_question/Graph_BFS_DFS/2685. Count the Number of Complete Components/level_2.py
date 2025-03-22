# 素直に各頂点が隣接している頂点を比較する
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        conponent_freq = defaultdict(int)

        for i in range(n):
            graph[i].append(i)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        for i in range(n):
            neighbors = tuple(sorted(graph[i]))
            conponent_freq[neighbors] += 1

        num_complete_component = 0
        for neighbors, freq in conponent_freq.items():
            if len(neighbors) == freq:
                num_complete_component += 1
        return num_complete_component


# UnionFindで解く
class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [1] * n

    def is_root(self, node):
        return self.parent[node] == -1

    def find_root(self, node):
        if self.is_root(node):
            return node
        self.parent[node] = self.find_root(self.parent[node])
        return self.parent[node]

    def marge_node(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if root1 == root2:
            return
        if self.size[root1] < self.size[root2]:
            small = root1
            big = root2
        else:
            small = root2
            big = root1
        self.parent[small] = big
        self.size[big] += self.size[small]


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge1, edge2 in edges:
            uf.marge_node(edge1, edge2)
        edge_count = [0] * n
        for edge1, edge2 in edges:
            root = uf.find_root(edge1)
            edge_count[root] += 1
        num_complete_component = 0
        for i in range(n):
            if not uf.is_root(i):
                continue
            num_node = uf.size[i]
            if edge_count[i] == num_node * (num_node - 1) // 2:
                num_complete_component += 1
        return num_complete_component
