# 問題の意味の理解に苦戦した。
# target以下のみを含む部分木と、targetより大きい値のみを含む部分木に分割する問題。
class Solution:
    def splitBST(
        self, root: Optional[TreeNode], target: int
    ) -> List[Optional[TreeNode]]:
        def helper(node):
            if not node:
                return None, None
            if node.val <= target:
                small_child, big_tree = helper(node.right)
                node.right = small_child
                return node, big_tree
            else:
                small_tree, big_child = helper(node.left)
                node.left = big_child
                return small_tree, node

        return helper(root)
