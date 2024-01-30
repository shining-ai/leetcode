# 幅優先探索
def solve_1(n, edges):
    all_nodes = set(range(n))
    seen = set()
    non_seen = all_nodes - seen
    net = [set() for _ in range(n)]
    ans = 0

    for i_edge in edges:
        net[i_edge[0]].add(i_edge[1])
        net[i_edge[1]].add(i_edge[0])

    while non_seen:
        stack = [non_seen.pop()]
        seen.add(stack[0])
        while stack:
            i_node = stack.pop()
            for i_child in net[i_node]:
                if i_child not in seen:
                    stack.append(i_child)
                    seen.add(i_child)

        non_seen = all_nodes - seen
        ans += 1

    return ans


# 深さ優先探索
def solve_2(n, edges):
    all_nodes = set(range(n))
    seen = set()
    non_seen = all_nodes - seen
    net = [set() for _ in range(n)]
    ans = 0

    for i_edge in edges:
        net[i_edge[0]].add(i_edge[1])
        net[i_edge[1]].add(i_edge[0])

    def dfs(i_node):
        seen.add(i_node)
        for i_child in net[i_node]:
            if i_child not in seen:
                dfs(i_child)

    while non_seen:
        dfs(non_seen.pop())
        ans += 1
        non_seen = all_nodes - seen

    return ans


# Union Find
def solve_3(n, edges):
    def find_root(x):
        while node[x] != -1:
            x = node[x]
        return x

    node = [-1 for i in range(n)]
    size = [1 for i in range(n)]
    root_node = set()

    for i_edge in edges:
        root_a = find_root(i_edge[0])
        root_b = find_root(i_edge[1])
        if root_a != root_b:
            if size[root_a] < size[root_b]:
                node[root_a] = root_b
                size[root_b] += size[root_a]
            else:
                node[root_b] = root_a
                size[root_a] += size[root_b]

    for i in range(n):
        root_node.add(find_root(i))

    return len(root_node)


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    # print(solve_1(n, edges))
    # print(solve_2(n, edges))
    print(solve_3(n, edges))
