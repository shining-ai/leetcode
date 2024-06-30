# BFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_queue = deque([(root, 0)])
        while node_queue:
            node, depth = node_queue.popleft()
            if not node.left and not node.right:
                break
            if node.left:
                node_queue.append((node.left, depth + 1))
            if node.right:
                node_queue.append((node.right, depth + 1))
        min_node_num = depth + 1
        return min_node_num


# DFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def search_min_depth(node):
            if not node.left and not node.right:
                return 0
            left_depth = float(inf)
            right_depth = float(inf)
            if node.left:
                left_depth = search_min_depth(node.left) + 1
            if node.right:
                right_depth = search_min_depth(node.right) + 1
            min_depth = min(left_depth, right_depth)
            return min_depth

        if not root:
            return 0
        min_node_num = search_min_depth(root) + 1
        return min_node_num


# DFSをstackで実装
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_depth_stack = [(root, 0)]
        min_depth = float(inf)
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
