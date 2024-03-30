# i件目までの家を見たときの最大値をcurrent_maxとする
# 家はループしているので、最初の家か最後の家を除いた2パターンを比較する
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
