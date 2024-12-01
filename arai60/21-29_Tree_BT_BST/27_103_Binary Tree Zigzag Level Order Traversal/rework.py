class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_nodes = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if not node:
                continue
            level_nodes[depth].append(node.val)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))d
        zigzag = list(level_nodes.values())
        for i, nodes in enumerate(zigzag):
            if i % 2 == 0:
                continue
            nodes.reverse()
        return zigzag
