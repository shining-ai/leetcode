# DFSでnodeを作成していく
# helper関数を使わない形に修正
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = (len(nums) - 1) // 2
        node = TreeNode(val=nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1 :])
        return node


# BFS
# queueの中身をlistに変更
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        queue = deque([(root, nums[:mid], nums[mid + 1 :])])
        while queue:
            node, left_nums, right_nums = queue.popleft()
            if left_nums:
                left_mid = (len(left_nums) - 1) // 2
                node.left = TreeNode(left_nums[left_mid])
                queue.append(
                    (
                        node.left,
                        left_nums[:left_mid],
                        left_nums[left_mid + 1 :],
                    )
                )
            if right_nums:
                right_mid = (len(right_nums) - 1) // 2
                node.right = TreeNode(right_nums[right_mid])
                queue.append(
                    (
                        node.right,
                        right_nums[:right_mid],
                        right_nums[right_mid + 1 :],
                    )
                )

        return root
