# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        traversal_index = 0

        def is_all_bar(start, end):
            if traversal[end] == "-":
                return False
            for i in range(start, end):
                if traversal[i] != "-":
                    return False
            return True

        def get_val(index):
            val = 0
            digit = 0
            while index < len(traversal) and traversal[index] != "-":
                val = val * 10 + int(traversal[index])
                digit += 1
                index += 1
            return digit, val

        def helper(depth):
            nonlocal traversal_index
            next_num_start = traversal_index + depth
            if len(traversal) <= next_num_start:
                return None
            if not is_all_bar(traversal_index, next_num_start):
                return None
            digit, val = get_val(next_num_start)
            node = TreeNode(val)
            traversal_index = next_num_start + digit
            node.left = helper(depth + 1)
            node.right = helper(depth + 1)
            return node

        return helper(0)
