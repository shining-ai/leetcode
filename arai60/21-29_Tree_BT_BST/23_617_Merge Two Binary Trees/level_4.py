# DFS(非破壊)
# レビューコメントを反映
# helper関数をなくした
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
            if not root2:
                return deepcopy(root1)
            if not root1:
                return deepcopy(root2)
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node

# BFS(非破壊)
# レビューコメントを反映
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        def merge_nodes(node1, node2):
            if not node2:
                return deepcopy(node1)
            if not node1:
                return deepcopy(node2)
            new_node = TreeNode(node1.val + node2.val)
            return new_node

        merged_root = merge_nodes(root1, root2)
        nodes_queue = deque()
        if root1 and root2:
            nodes_queue.append((merged_root, root1, root2))
        while nodes_queue:
            merged_node, node1, node2 = nodes_queue.popleft()
            merged_node.left = merge_nodes(node1.left, node2.left)
            merged_node.right = merge_nodes(node1.right, node2.right)
            if node1.left and node2.left:
                nodes_queue.append((merged_node.left, node1.left, node2.left))
            if node1.right and node2.right:
                nodes_queue.append((merged_node.right, node1.right, node2.right))
        return merged_root
