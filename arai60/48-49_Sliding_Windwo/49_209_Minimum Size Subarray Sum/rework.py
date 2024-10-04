class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = math.inf
        current = 0
        for right, num in enumerate(nums):
            current += num
            while current >= target:
                min_length = min(min_length, right - left + 1)
                current -= nums[left]
                left += 1
        if min_length == math.inf:
            min_length = 0
        return min_length
