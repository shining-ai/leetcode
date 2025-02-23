# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        val_to_postorder_index = {}
        for i, val in enumerate(postorder):
            val_to_postorder_index[val] = i

        def helper(index):
            nonlocal preorder_index
            if preorder_index >= len(preorder):
                return None
            val = preorder[preorder_index]
            postorder_index = val_to_postorder_index[val]
            if postorder_index >= index:
                return None
            node = TreeNode(val)
            preorder_index += 1
            node.left = helper(postorder_index)
            node.right = helper(postorder_index)

            return node

        return helper(len(preorder))
