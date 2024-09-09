# 前から順に足していき、最大値を更新していく
# 途中で負の値になったら、その次の要素は0からスタートしたほうが大きくなる
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_subarray = -math.inf
        current_sum_subarray = 0
        for num in nums:
            current_sum_subarray += num
            max_sum_subarray = max(max_sum_subarray, current_sum_subarray)
            if current_sum_subarray < 0:
                current_sum_subarray = 0
        return max_sum_subarray
