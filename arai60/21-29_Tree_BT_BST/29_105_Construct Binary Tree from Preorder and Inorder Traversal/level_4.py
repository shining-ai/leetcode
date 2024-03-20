#  [inorder_left, inorder_right) 右側を開区間に修正
class Solution:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        inorder_index_map = {}
        for i, val in enumerate(inorder):
            inorder_index_map[val] = i

        current_preorder_index = 0

        def array_to_tree(inorder_left, inorder_right):
            nonlocal current_preorder_index
            if inorder_left >= inorder_right:
                return None
            val = preorder[current_preorder_index]
            node = TreeNode(val)
            inorder_index = inorder_index_map[val]
            current_preorder_index += 1
            node.left = array_to_tree(inorder_left, inorder_index)
            node.right = array_to_tree(inorder_index + 1, inorder_right)
            return node

        return array_to_tree(0, len(inorder))
