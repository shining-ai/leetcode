# DFS(再帰)
# 変更なし
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            if root.val == targetSum:
                return True
        diff_target = targetSum - root.val
        return self.hasPathSum(root.left, diff_target) or self.hasPathSum(root.right, diff_target)


# DFS(stack)
# leafのチェックを関数化
# leafの場合、continueするように変更
# is_leafの条件を反転してネストを浅くした
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_leaf(node):
            return not node.left and not node.right

        node_sum_stack = [(root, 0)]
        while node_sum_stack:
            node, path_sum = node_sum_stack.pop()
            if not node:
                continue
            path_sum += node.val
            if not is_leaf(node):
                node_sum_stack.append((node.right, path_sum))
                node_sum_stack.append((node.left, path_sum))
                continue
            if path_sum == targetSum:
                return True
        return False


# BFS
# leafのチェックを関数化
# leafの場合、continueするように変更
# is_leafの条件を反転してネストを浅くした
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_leaf(node):
            return not node.left and not node.right

        node_sum_queue = deque([(root, 0)])
        while node_sum_queue:
            node, path_sum = node_sum_queue.popleft()
            if not node:
                continue
            path_sum += node.val
            if not is_leaf(node):
                node_sum_queue.append((node.left, path_sum))
                node_sum_queue.append((node.right, path_sum))
                continue
            if path_sum == targetSum:
                return True
        return False
