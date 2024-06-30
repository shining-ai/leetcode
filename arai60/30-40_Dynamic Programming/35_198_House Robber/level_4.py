# DP
# 全軒の情報は使わないので、変数を2つだけ使う
# 変数名をcurrentからmax_currentに変更
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_amount_2_before = 0
        max_amount_1_before = nums[0]
        for num in nums[1:]:
            max_current = max(max_amount_2_before + num, max_amount_1_before)
            max_amount_2_before = max_amount_1_before
            max_amount_1_before = max_current
        return max_amount_1_before
