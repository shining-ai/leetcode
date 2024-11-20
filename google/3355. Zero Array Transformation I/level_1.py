# 累積和を使った解放
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        cumulative = [0] * (len(nums) + 1)
        for query in queries:
            cumulative[query[0]] += 1
            cumulative[query[1] + 1] -= 1
        cumulative_sum = 0
        for i, num in enumerate(nums):
            cumulative_sum += cumulative[i]
            if num > cumulative_sum:
                return False
        return True
