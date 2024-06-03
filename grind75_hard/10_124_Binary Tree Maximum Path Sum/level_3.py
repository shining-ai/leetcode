
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            left_sum = max(0, helper(node.left))
            right_sum = max(0, helper(node.right))
            max_sum = max(max_sum, node.val + left_sum + right_sum)
            return max(node.val + left_sum, node.val + right_sum)

        helper(root)
        return max_sum
