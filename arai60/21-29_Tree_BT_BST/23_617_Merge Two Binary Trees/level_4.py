# DFS(非破壊)
# レビューコメントを反映
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def helper_merge_trees(node1, node2):
            if not node2:
                return node1
            if not node1:
                return deepcopy(node2)
            node1.val += node2.val
            node1.left = helper_merge_trees(node1.left, node2.left)
            node1.right = helper_merge_trees(node1.right, node2.right)
            return node1

        root1_clone = deepcopy(root1)
        return helper_merge_trees(root1_clone, root2)


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
