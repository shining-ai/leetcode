# BFSで解く
# queueにNoneが入らないように修正
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        node_queue = deque([root])
        level_order = []
        while node_queue:
            num_nodes_in_level = len(node_queue)
            nodes_in_level = []
            for _ in range(num_nodes_in_level):
                node = node_queue.popleft()
                nodes_in_level.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            level_order.append(nodes_in_level)
        return level_order


# DFSで解く
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level_order = []

        def build_level_order(node, level):
            while len(level_order) - 1 < level:
                level_order.append([])
            level_order[level].append(node.val)
            if node.left:
                build_level_order(node.left, level + 1)
            if node.right:
                build_level_order(node.right, level + 1)

        build_level_order(root, 0)
        return level_order
