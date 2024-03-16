# BFS
# 変数名を修正
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        node_queue = deque([root])
        zigzag_order = []
        level = 0
        while node_queue:
            num_node_in_level = len(node_queue)
            values_in_level = []
            for _ in range(num_node_in_level):
                node = node_queue.popleft()
                values_in_level.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            if level % 2:
                values_in_level.reverse()
            zigzag_order.append(values_in_level)
            level += 1
        return zigzag_order
