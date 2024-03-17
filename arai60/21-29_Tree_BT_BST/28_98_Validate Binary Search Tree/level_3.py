class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper_valid_bst(node, min_val=-math.inf, max_val=math.inf):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False
            is_left_valid = helper_valid_bst(node.left, min_val, node.val)
            is_right_valid = helper_valid_bst(node.right, node.val, max_val)
            return is_left_valid and is_right_valid

        return helper_valid_bst(root)
