# level_1から変更なし
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_max(nums):
            max_amount_2_before = 0
            max_amount_1_before = nums[0]
            for num in nums[1:]:
                current_max = max(max_amount_2_before + num, max_amount_1_before)
                max_amount_2_before = max_amount_1_before
                max_amount_1_before = current_max
            return max_amount_1_before

        return max(rob_max(nums[1:]), rob_max(nums[:-1]))
