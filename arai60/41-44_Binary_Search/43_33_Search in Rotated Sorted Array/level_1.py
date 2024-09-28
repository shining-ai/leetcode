# 最小値(pivot)を見つけてそこで左右に分割して考える。
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot_index():
            left = 0
            right = len(nums) - 1
            while left < right:
                middle = (left + right) // 2
                if nums[middle] < nums[right]:
                    right = middle
                else:
                    left = middle + 1
            return left

        pivot_index = find_pivot_index()
        if nums[pivot_index] <= target <= nums[-1]:
            left = pivot_index
            right = len(nums)
        else:
            left = 0
            right = pivot_index
        target_index = bisect.bisect_left(nums, target, left, right)
        if nums[target_index] == target:
            return target_index
        return -1
