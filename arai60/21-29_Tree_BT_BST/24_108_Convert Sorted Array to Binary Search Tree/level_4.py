# DFSでnodeを作成していく(再帰①)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = (len(nums) - 1) // 2
        node = TreeNode(val=nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])  # 帰りがけの作業
        node.right = self.sortedArrayToBST(nums[mid + 1 :])  # 帰りがけの作業
        return node


# DFSでnodeを作成していく(再帰②)
# 呼び出された側でnodeの書き込みまで行う
# rootだけは別途作成が必要
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(node, index, nums):
            left_nums = nums[:index]
            if left_nums:
                left_mid = (len(left_nums) - 1) // 2
                node.left = TreeNode(val=left_nums[left_mid])
                helper(node.left, left_mid, left_nums)
            right_nums = nums[index + 1 :]
            if right_nums:
                right_mid = (len(right_nums)) // 2
                node.right = TreeNode(val=right_nums[right_mid])
                helper(node.right, right_mid, right_nums)

        mid = (len(nums) - 1) // 2
        root = TreeNode(val=nums[mid])
        helper(root, mid, nums)
        return root


# 再帰②をstackで実装
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = (len(nums) - 1) // 2
        root = TreeNode(val=nums[mid])
        stack = [(root, mid, nums)]

        while stack:
            node, index, nums_list = stack.pop()
            left_nums = nums_list[:index]
            if left_nums:
                left_mid = (len(left_nums) - 1) // 2
                node.left = TreeNode(val=left_nums[left_mid])
                stack.append((node.left, left_mid, left_nums))
            right_nums = nums_list[index + 1 :]
            if right_nums:
                right_mid = (len(right_nums)) // 2
                node.right = TreeNode(val=right_nums[right_mid])
                stack.append((node.right, right_mid, right_nums))

        return root


# BFS
# queueの中身をlistに変更
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def create_child(child_nums):
            if not child_nums:
                return 0, None
            mid = (len(child_nums) - 1) // 2
            child = TreeNode(child_nums[mid])
            return mid, child

        if not nums:
            return None
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        queue = deque([(root, nums[:mid], nums[mid + 1 :])])
        while queue:
            parent, left_nums, right_nums = queue.popleft()
            left_mid, parent.left = create_child(left_nums)
            if parent.left:
                queue.append((parent.left, left_nums[:left_mid], left_nums[left_mid + 1 :]))
            right_mid, parent.right = create_child(right_nums)
            if parent.right:
                queue.append((parent.right, right_nums[:right_mid], right_nums[right_mid + 1 :]))
        return root
