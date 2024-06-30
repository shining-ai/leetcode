# BFSで解く
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_queue = deque([root])
        level_order = []
        while node_queue:
            node_num = len(node_queue)
            nodes = []
            for _ in range(node_num):
                node = node_queue.popleft()
                if not node:
                    continue
                nodes.append(node.val)
                node_queue.append(node.left)
                node_queue.append(node.right)
            if nodes:
                level_order.append(nodes)
        return level_order
