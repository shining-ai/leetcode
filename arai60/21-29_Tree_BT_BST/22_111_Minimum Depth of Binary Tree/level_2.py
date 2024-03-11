# BFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_depth_queue = deque([(root, 0)])
        while node_depth_queue:
            node, depth = node_depth_queue.popleft()
            if not node.left and not node.right:
                return depth + 1
            if node.left:
                node_depth_queue.append((node.left, depth + 1))
            if node.right:
                node_depth_queue.append((node.right, depth + 1))


# DFS
# left_depthとright_depthをmin_depthに統合
# min_depthの初期値をintの最大値に変更
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = sys.maxsize
        if root.left:
            min_depth = min(min_depth, self.minDepth(root.left) + 1)
        if root.right:
            min_depth = min(min_depth, self.minDepth(root.right) + 1)
        return min_depth


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
        return min_depth + 1
