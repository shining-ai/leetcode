# indexまでの要素を使った最大値をすべて求めて比較する
# listにしなくても、2変数あれば実装できた
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # indexまでの要素を使った最大値
        current_sum_subarray = nums[0]
        max_sum_subarray = nums[0]

        for i in range(1, len(nums)):
            current_sum_subarray = max(current_sum_subarray + nums[i], nums[i])
            max_sum_subarray = max(max_sum_subarray, current_sum_subarray)

        return max_sum_subarray


# Divide and Conquer(解答に載っていた手法)
# 真ん中から外側に向かって最大値を求め、真ん中をつなげる
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def find_max_sum_subarray(left, right):
            if left >= right:
                return -math.inf
            mid = (left + right) // 2
            curr = 0
            max_sum_left = 0
            max_sum_right = 0
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                max_sum_left = max(max_sum_left, curr)
            curr = 0
            for i in range(mid + 1, right):
                curr += nums[i]
                max_sum_right = max(max_sum_right, curr)
            max_sum_combined = nums[mid] + max_sum_left + max_sum_right
            max_sum_left_half = find_max_sum_subarray(left, mid)
            max_sum_right_half = find_max_sum_subarray(mid + 1, right)
            return max(max_sum_combined, max_sum_left_half, max_sum_right_half)

        return find_max_sum_subarray(0, len(nums))
