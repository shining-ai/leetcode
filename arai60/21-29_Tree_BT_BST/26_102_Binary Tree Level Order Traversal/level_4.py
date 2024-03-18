# BFS
# queueの中身の個数でレベルを判定していた部分を修正(current_queue, next_queueを使うように修正)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level_order = []
        current_queue = deque([root])
        while current_queue:
            nodes_in_level = []
            next_queue = deque()
            while current_queue:
                node = current_queue.popleft()
                nodes_in_level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            level_order.append(nodes_in_level)
            current_queue = next_queue
        return level_order
