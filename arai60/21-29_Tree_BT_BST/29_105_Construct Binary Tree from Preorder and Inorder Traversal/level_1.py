class Solution:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        current_preorder_index = 0

        def array_to_tree(split_inorder):
            nonlocal current_preorder_index
            if current_preorder_index >= len(preorder):
                return None
            val = preorder[current_preorder_index]
            if not val in split_inorder:
                return None
            current_preorder_index += 1
            node = TreeNode(val)
            inorder_index = split_inorder.index(val)
            node.left = array_to_tree(split_inorder[:inorder_index])
            node.right = array_to_tree(split_inorder[inorder_index + 1 :])
            return node

        return array_to_tree(inorder)
