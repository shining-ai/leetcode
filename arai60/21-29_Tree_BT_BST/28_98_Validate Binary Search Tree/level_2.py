# DFS(再帰)
# 再帰部分の戻り値を変数に格納
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper_valid_bst(node, min_val=-math.inf, max_val=math.inf):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False
            if not helper_valid_bst(node.left, min_val, node.val):
                return False
            if not helper_valid_bst(node.right, node.val, max_val):
                return False
            return True

        return helper_valid_bst(root)


# DFS(スタック)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node_range_stack = [(root, -math.inf, math.inf)]
        while node_range_stack:
            node, min_val, max_val = node_range_stack.pop()
            if not node:
                continue
            if not min_val < node.val < max_val:
                return False
            node_range_stack.append((node.right, node.val, max_val))
            node_range_stack.append((node.left, min_val, node.val))
        return True


# BFS
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node_range_queue = deque([(root, -math.inf, math.inf)])
        while node_range_queue:
            node, min_val, max_val = node_range_queue.popleft()
            if not node:
                continue
            if not min_val < node.val < max_val:
                return False
            node_range_queue.append((node.left, min_val, node.val))
            node_range_queue.append((node.right, node.val, max_val))
        return True
