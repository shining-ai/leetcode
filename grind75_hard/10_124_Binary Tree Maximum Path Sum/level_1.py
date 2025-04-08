# DFSを使う
# 子を2つ持てるのは根だけ
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float("inf")

        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            left_sum = helper(node.left)
            right_sum = helper(node.right)
            one_child_val = max(node.val + left_sum, node.val + right_sum)
            two_child_val = node.val + left_sum + right_sum
            max_sum = max(max_sum, node.val, one_child_val, two_child_val)
            return max(node.val, one_child_val)

        helper(root)
        return max_sum
