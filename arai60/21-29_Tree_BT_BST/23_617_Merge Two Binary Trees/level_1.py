# DFS(破壊的)
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root2:
            return root1
        if not root1:
            return root2
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


# BFS(破壊的)
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        if not root1:
            return root2
        if not root2:
            return root1
        nodes_queue = deque([(root1, root2)])
        root1.val += root2.val
        while nodes_queue:
            node1, node2 = nodes_queue.popleft()
            if node1.left and node2.left:
                node1.left.val += node2.left.val
                nodes_queue.append((node1.left, node2.left))
            if not node1.left:
                node1.left = node2.left
            if node1.right and node2.right:
                assert node1.right and node2.right
                node1.right.val += node2.right.val
                nodes_queue.append((node1.right, node2.right))
            if not node1.right:
                node1.right = node2.right
        return root1
