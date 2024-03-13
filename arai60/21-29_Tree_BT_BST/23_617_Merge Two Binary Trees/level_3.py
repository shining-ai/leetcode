class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def helper_merge_tree(node1, node2):
            if not node1 and not node2:
                return None
            if not node1:
                return node2
            if not node2:
                return node1
            node1.val += node2.val
            node1.left = helper_merge_tree(node1.left, node2.left)
            node1.right = helper_merge_tree(node1.right, node2.right)
            return node1

        sum_tree = deepcopy(root1)
        return helper_merge_tree(sum_tree, root2)
