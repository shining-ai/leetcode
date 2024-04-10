# 解答を見て実装
# targetより大きい時はそれより右側は確認する必要なし
# targetより小さい時はそれより左側は確認する必要なし
class Solution:
    def splitBST(
        self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        def cut_bst(node):
            if not node:
                return [None, None]
            if node.val <= target:
                left, right = cut_bst(node.right)
                node.right = left
                return [node, right]
            left, right = cut_bst(node.left)
            node.left = right
            return [left, node]

        return cut_bst(root)
