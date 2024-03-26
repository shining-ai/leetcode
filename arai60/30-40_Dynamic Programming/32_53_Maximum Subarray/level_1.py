# indexまでの要素を使った最大値をすべて求めて比較する
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # indexまでの要素を使った最大値
        max_sum_end_as_index = [-math.inf] * len(nums)
        max_sum_end_as_index[0] = nums[0]

        for i in range(1, len(nums)):
            max_sum_end_as_index[i] = max(
                max_sum_end_as_index[i - 1] + nums[i], nums[i]
            )
        return max(max_sum_end_as_index)

