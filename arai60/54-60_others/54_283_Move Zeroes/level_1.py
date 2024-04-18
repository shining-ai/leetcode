# 0を見つけたら削除して末尾に追加する
# 要素を削除するとインデックスがずれるので、O(n^2)になる
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zero = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                num_zero += 1
            else:
                i += 1
        nums += [0] * num_zero


# 確定済みの要素を記憶しておく
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        last_fixed_index = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[last_fixed_index + 1], nums[i] = nums[i], nums[last_fixed_index + 1]
            last_fixed_index += 1
