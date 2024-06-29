# indexの変数名をnon_zeros_lengthに変更
# zoroを複数形に変更
# swapせずに最後に一括で0を代入する
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeros_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[non_zeros_length] = nums[i]
            non_zeros_length += 1
        for i in range(non_zeros_length, len(nums)):
            nums[i] = 0
