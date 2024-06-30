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
