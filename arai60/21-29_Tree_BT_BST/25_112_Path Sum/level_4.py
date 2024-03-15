# DFS(再帰)
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        diff_target = targetSum - root.val
        return self.hasPathSum(root.left, diff_target) or self.hasPathSum(root.right, diff_target)
