# DP
# 全軒の情報は使わないので、変数を2つだけ使う
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_amount_2_before = 0
        max_amount_1_before = nums[0]
        for num in nums[1:]:
            current = max(max_amount_2_before + num, max_amount_1_before)
            max_amount_2_before = max_amount_1_before
            max_amount_1_before = current
        return max_amount_1_before
