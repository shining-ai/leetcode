# BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        node_queue = deque([root])
        level_order = []
        while node_queue:
            queue_length = len(node_queue)
            nodes = []
            for _ in range(queue_length):
                node = node_queue.popleft()
                nodes.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            level_order.append(nodes)
        return level_order
