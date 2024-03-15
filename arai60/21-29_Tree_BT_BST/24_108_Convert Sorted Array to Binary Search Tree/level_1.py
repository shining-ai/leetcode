# DFS
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node

        return helper(0, len(nums) - 1)


# BFS
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        queue = deque([(root, (0, mid - 1), (mid + 1, len(nums) - 1))])
        while queue:
            node, left_range, right_range = queue.popleft()
            if left_range[0] <= left_range[1]:
                left_mid = (left_range[0] + left_range[1]) // 2
                node.left = TreeNode(nums[left_mid])
                queue.append(
                    (
                        node.left,
                        (left_range[0], left_mid - 1),
                        (left_mid + 1, left_range[1]),
                    )
                )
            if right_range[0] <= right_range[1]:
                right_mid = (right_range[0] + right_range[1]) // 2
                node.right = TreeNode(nums[right_mid])
                queue.append(
                    (
                        node.right,
                        (right_range[0], right_mid - 1),
                        (right_mid + 1, right_range[1]),
                    )
                )

        return root
