# DP
# i軒目までの家を見たときの最大の金額をdp[i]とする
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums, default=0)
        max_robbed_amount = [0] * len(nums)
        max_robbed_amount[0] = nums[0]
        max_robbed_amount[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_robbed_amount[i] = max(
                max_robbed_amount[i - 2] + nums[i],
                max_robbed_amount[i - 1],
            )
        return max_robbed_amount[-1]
