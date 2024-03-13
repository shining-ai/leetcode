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

        def merge_nodes(node1, node2, queue):
            if node1 and node2:
                node1.val += node2.val
                queue.append((node1, node2))
            if not node1:
                node1 = node2
            return node1, queue

        nodes_queue = deque()
        root1_clone = deepcopy(root1)
        root1_clone, nodes_queue = merge_nodes(root1_clone, root2, nodes_queue)
        while nodes_queue:
            node1, node2 = nodes_queue.popleft()
            node1.left, nodes_queue = merge_nodes(node1.left, node2.left, nodes_queue)
            node1.right, nodes_queue = merge_nodes(node1.right, node2.right, nodes_queue)
        return root1_clone
