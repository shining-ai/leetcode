# indexまでの要素を使った最大値をすべて求めて比較する
# listにしなくても、2変数あれば実装できた
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # indexまでの要素を使った最大値
        current_max_subarray = nums[0]
        overall_max_subarray = nums[0]

        for i in range(1, len(nums)):
            current_max_subarray = max(current_max_subarray + nums[i], nums[i])
            overall_max_subarray = max(
                overall_max_subarray, current_max_subarray
            )

        return overall_max_subarray


# Divide and Conquer(解答に載っていた手法)
# コメントの内容を反映
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def calculate_max_sum_subarray(left, right, reverse=False):
            direction = 1
            if reverse:
                direction = -1
            curr = 0
            overall_max_subarray = 0
            for i in range(left, right, direction):
                curr += nums[i]
                overall_max_subarray = max(overall_max_subarray, curr)
            return overall_max_subarray

        def find_max_sum_subarray(left, right):
            if left >= right:
                return -math.inf
            middle = (left + right) // 2
            max_sum_left = calculate_max_sum_subarray(
                middle - 1, left - 1, reverse=True
            )
            max_sum_right = calculate_max_sum_subarray(middle + 1, right)
            max_sum_combined = nums[middle] + max_sum_left + max_sum_right
            max_sum_left_half = find_max_sum_subarray(left, middle)
            max_sum_right_half = find_max_sum_subarray(middle + 1, right)
            return max(max_sum_combined, max_sum_left_half, max_sum_right_half)

        return find_max_sum_subarray(0, len(nums))
