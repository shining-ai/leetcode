# DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def search_max_depth(node):
            if not node:
                return 0
            left_depth = search_max_depth(node.left) + 1
            right_depth = search_max_depth(node.right) + 1
            max_depth = max(left_depth, right_depth)
            return max_depth

        return search_max_depth(root)


# BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_depth_queue = deque([(root, 1)])
        max_depth = 0
        while node_depth_queue:
            node, depth = node_depth_queue.popleft()
            if node.left:
                node_depth_queue.append((node.left, depth + 1))
            if node.right:
                node_depth_queue.append((node.right, depth + 1))
            max_depth = max(max_depth, depth)
        return max_depth


# stackで深さ優先探索
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack_node_depth = [(root, 1)]
        max_depth = 1
        while stack_node_depth:
            node, depth = stack_node_depth.pop()
            if node.left:
                stack_node_depth.append((node.left, depth + 1))
            if node.right:
                stack_node_depth.append((node.right, depth + 1))
            max_depth = max(max_depth, depth)
        return max_depth
