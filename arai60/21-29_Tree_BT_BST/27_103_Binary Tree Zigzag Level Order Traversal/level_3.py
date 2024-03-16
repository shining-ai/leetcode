class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        node_queue = deque([root])
        zigzag_order = []
        level = 0
        while node_queue:
            num_node_in_level = len(node_queue)
            nodes = []
            for _ in range(num_node_in_level):
                node = node_queue.popleft()
                nodes.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            if level % 2 == 1:
                nodes.reverse()
            zigzag_order.append(nodes)
            level += 1
        return zigzag_order
