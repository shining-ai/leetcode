class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        max_amount_before_1 = 0
        max_current = 0
        for num in nums:
            max_amount_before_2 = max_amount_before_1
            max_amount_before_1 = max_current
            max_current = max(max_amount_before_2 + num, max_amount_before_1)
        return max_current
