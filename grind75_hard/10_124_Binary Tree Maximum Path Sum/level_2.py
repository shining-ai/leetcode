# 子ノードが負の場合は、その子ノードを選ばない(0にする)ように修正
# root.valを初期値にしておく
# 一応rootがNoneの場合は0を返すようにする
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_sum = root.val

        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            left_sum = max(0, helper(node.left))
            right_sum = max(0, helper(node.right))
            max_sum = max(max_sum, node.val + left_sum + right_sum)
            return node.val + max(left_sum, right_sum)

        helper(root)
        return max_sum
