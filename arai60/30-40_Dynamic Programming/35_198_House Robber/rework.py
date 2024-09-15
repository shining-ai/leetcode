class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        max_amount_before_2 = 0
        max_amount_before_1 = 0
        for num in nums:
            current_max = max(max_amount_before_2 + num, max_amount_before_1)
            max_amount_before_2 = max_amount_before_1
            max_amount_before_1 = current_max
        return current_max
