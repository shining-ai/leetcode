# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper_is_valid(node, upper, lower):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return helper_is_valid(node.left, node.val, lower) and helper_is_valid(
                node.right, upper, node.val
            )

        return helper(root, inf, -inf)
