# BFS
# levelを上げるタイミングを変更
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


# DFS
# zigzag_orderへの追加を関数に切り出す
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        zigzag_order = []

        def append_zigzag_order(node, level):
            if level % 2 == 0:
                zigzag_order[level].append(node.val)
            else:
                zigzag_order[level].appendleft(node.val)

        def build_zigzag_order(node, level):
            while len(zigzag_order) - 1 < level:
                zigzag_order.append(deque())
            append_zigzag_order(node, level)
            if node.left:
                build_zigzag_order(node.left, level + 1)
            if node.right:
                build_zigzag_order(node.right, level + 1)

        build_zigzag_order(root, 0)
        return zigzag_order
