# level_1から特に変更なし
# bisectモジュールのソースとも同じ実装
# https://github.com/python/cpython/blob/3.12/Lib/bisect.py#L74
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left
