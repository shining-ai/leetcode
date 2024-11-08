# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = defaultdict(list)

        def helper(node):
            if not node:
                return -1
            bottom_level = max(helper(node.left), helper(node.right)) + 1
            leaves[bottom_level].append(node.val)
            return bottom_level

        helper(root)
        return list(leaves.values())
