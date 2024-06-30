# DFS
# 特に変更なし
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1
        max_depth = max(left_depth, right_depth)
        return max_depth


# BFS
# 特に変更なし
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_depth_queue = deque([(root, 1)])
        while node_depth_queue:
            node, depth = node_depth_queue.popleft()
            if node.left:
                node_depth_queue.append((node.left, depth + 1))
            if node.right:
                node_depth_queue.append((node.right, depth + 1))
        max_depth = depth
        return max_depth


# stackで深さ優先探索
# 特に変更なし
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
