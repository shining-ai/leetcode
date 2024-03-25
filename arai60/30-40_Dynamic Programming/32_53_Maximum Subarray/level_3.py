class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum_subarray = nums[0]
        max_sum_subarray = nums[0]
        for num in nums[1:]:
            current_sum_subarray = max(current_sum_subarray + num, num)
            max_sum_subarray = max(max_sum_subarray, current_sum_subarray)
        return max_sum_subarray
