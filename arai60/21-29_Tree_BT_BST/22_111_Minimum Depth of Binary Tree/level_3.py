
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
