class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper_valid_bst(node, lower=-math.inf, upper=math.inf):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            if not helper_valid_bst(node.left, lower, node.val):
                return False
            if not helper_valid_bst(node.right, node.val, upper):
                return False
            return True

        return helper_valid_bst(root)
