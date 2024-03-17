class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper_valid_bst(node, min_val=-math.inf, max_val=math.inf):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False
            if not helper_valid_bst(node.left, min_val, node.val):
                return False
            if not helper_valid_bst(node.right, node.val, max_val):
                return False
            return True

        return helper_valid_bst(root)
