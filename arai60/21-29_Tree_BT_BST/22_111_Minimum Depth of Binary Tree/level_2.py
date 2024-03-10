# BFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_depth_queue = deque([(root, 0)])
        while node_depth_queue:
            node, depth = node_depth_queue.popleft()
            if not node.left and not node.right:
                break
            if node.left:
                node_depth_queue.append((node.left, depth + 1))
            if node.right:
                node_depth_queue.append((node.right, depth + 1))
        min_node_num = depth + 1
        return min_node_num


# DFS
# left_depthとright_depthをmin_depthに統合
# min_depthの初期値をintの最大値に変更
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def search_min_depth(node):
            if not node.left and not node.right:
                return 0
            min_depth = sys.maxsize
            if node.left:
                min_depth = min(min_depth, search_min_depth(node.left) + 1)
            if node.right:
                min_depth = min(min_depth, search_min_depth(node.right) + 1)
            return min_depth

        if not root:
            return 0
        min_node_num = search_min_depth(root) + 1
        return min_node_num


# DFSをstackで実装
# min_depthの初期値をintの最大値に変更
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_depth_stack = [(root, 0)]
        min_depth = sys.maxsize
        while node_depth_stack:
            node, depth = node_depth_stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
                continue
            if node.right:
                node_depth_stack.append((node.right, depth + 1))
            if node.left:
                node_depth_stack.append((node.left, depth + 1))
        min_node_num = min_depth + 1
        return min_node_num
