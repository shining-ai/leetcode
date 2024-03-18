# BFS
# 変数名を修正
# queueの中身の個数でlevelを判定していた部分を修正(current_queueとnext_queueを使うように変更)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        current_queue = deque([root])
        zigzag_order = []
        level = 0
        while current_queue:
            values_in_level = []
            next_queue = deque()
            while current_queue:
                node = current_queue.popleft()
                values_in_level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if level % 2:
                values_in_level.reverse()
            zigzag_order.append(values_in_level)
            level += 1
            current_queue = next_queue
        return zigzag_order


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
        zigzag_order = list(map(list, zigzag_order))
        return zigzag_order
