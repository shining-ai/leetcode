# 関数を作成せずに再帰で解く
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]
        if root.val <= target:
            smaller_tree, greater_tree = self.splitBST(root.right, target)
            root.right = smaller_tree
            return [root, greater_tree]
        smaller_tree, greater_tree = self.splitBST(root.left, target)
        root.left = greater_tree
        return [smaller_tree, root]



