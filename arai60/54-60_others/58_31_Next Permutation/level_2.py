# 操作を関数化して、見通しを良くする
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def find_index_not_ascending_from_end(nums):
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    return i
            return -1

        def find_index_next_larger(nums, target_index):
            min_value = math.inf
            for i in range(target_index + 1, len(nums)):
                if nums[target_index] < nums[i] < min_value:
                    min_value = nums[i]
                    index = i
            return index

        left = find_index_not_ascending_from_end(nums)
        if left == -1:
            nums.reverse()
            return
        right = find_index_next_larger(nums, left)
        nums[left], nums[right] = nums[right], nums[left]
        nums[left + 1 :] = sorted(nums[left + 1 :])
