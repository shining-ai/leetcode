# Union-Findで解く
class UnionFind:
    def __init__(self, n):
        self.size = [1] * n
        self.parent = [-1] * n
        self.val = [2**20 - 1] * n

    def is_root(self, node):
        return self.parent[node] == -1

    def find_root(self, node):
        root = node
        while not self.is_root(root):
            val = self.val[root]
            root = self.parent[root]
            self.val[root] &= val
        while not self.is_root(node):
            next_node = self.parent[node]
            self.parent[node] = root
            node = next_node
        return root

    def marge_node(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if root1 == root2:
            return
        if self.size[root1] < self.size[root2]:
            big = root2
            small = root1
        else:
            big = root1
            small = root2
        self.parent[small] = big
        self.size[big] += self.size[small]
        self.val[big] &= self.val[small]


class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:

        uf = UnionFind(n)
        for u, v, w in edges:
            uf.val[u] &= w
            uf.val[v] &= w
            uf.marge_node(u, v)

        query_ans = []
        for s, t in query:
            root_s = uf.find_root(s)
            root_t = uf.find_root(t)
            if root_s != root_t:
                query_ans.append(-1)
            else:
                query_ans.append(uf.val[root_s])
        return query_ans
