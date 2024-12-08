# ボトムアップ
class Solution:
    def rob(self, nums: List[int]) -> int:
        current_max = 0
        max_amount_before_1 = 0
        max_amount_before_2 = 0
        for num in nums:
            current_max = max(max_amount_before_1, max_amount_before_2 + num)
            max_amount_before_2 = max_amount_before_1
            max_amount_before_1 = current_max
        return current_max


# トップダウン
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def helper(index):
            if index < 0:
                return 0
            max_amount = max(helper(index - 1), helper(index - 2) + nums[index])
            return max_amount

        return helper(len(nums) - 1)
