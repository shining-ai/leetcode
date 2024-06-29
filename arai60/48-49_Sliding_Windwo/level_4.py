class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        min_length = len(nums)
        left = 0
        current_sum = 0
        for right in range(1, len(nums) + 1):
            current_sum += nums[right - 1]
            while target <= current_sum:
                min_length = min(min_length, right - left)
                current_sum -= nums[left]
                left += 1
        return min_length
