# DFS(再帰)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper_valid_bst(node, min_val=-math.inf, max_val=math.inf):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False
            return helper_valid_bst(
                node.left, min_val, node.val
            ) and helper_valid_bst(node.right, node.val, max_val)

        return helper_valid_bst(root)
