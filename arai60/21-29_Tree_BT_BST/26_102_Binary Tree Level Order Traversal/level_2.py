# BFSで解く
# queueにNoneが入らないように修正
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        node_queue = deque([root])
        level_order = []
        while node_queue:
            queue_length = len(node_queue)
            level_nodes = []
            for _ in range(queue_length):
                node = node_queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            level_order.append(level_nodes)
        return level_order


# DFSで解く
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level_order = []

        def build_level_order(node, level):
            if len(level_order) - 1 < level:
                level_order.append([])
            level_order[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return level_order
