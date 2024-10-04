class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = math.inf
        left = 0
        current_sum = 0
        for right in range(1, len(nums) + 1):
            current_sum += nums[right - 1]
            while target <= current_sum:
                min_length = min(min_length, right - left)
                current_sum -= nums[left]
                left += 1
        if min_length == math.inf:
            return 0
        return min_length
