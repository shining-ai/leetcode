# 最大値を引数で渡すように修正
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def helper(node, max_sum):
            if not node:
                return 0, max_sum
            left_sum, max_sum = helper(node.left, max_sum)
            right_sum, max_sum = helper(node.right, max_sum)
            max_sum = max(max_sum, node.val + left_sum + right_sum)
            max_one_child = node.val + max(left_sum, right_sum)
            return max(0, max_one_child), max_sum

        _, max_sum = helper(root, root.val)
        return max_sum
