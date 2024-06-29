# 確定済みの要素を記憶しておく
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        first_zero_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[first_zero_index], nums[i] = (nums[i], nums[first_zero_index])
            first_zero_index += 1
