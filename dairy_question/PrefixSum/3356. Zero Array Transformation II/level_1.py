# 累積和と二分探索を使う
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def n_queries(n: int):
            difference_array = [0] * (len(nums) + 1)
            for i in range(n):
                l, r, val = queries[i]
                difference_array[l] += val
                difference_array[r + 1] -= val
            prefix_sum = [0]
            for difference in difference_array:
                prefix_sum.append(prefix_sum[-1] + difference)
            return prefix_sum[1:]

        def is_non_negative(nums_array):
            for i, j in zip(nums, nums_array):
                if i > j:
                    return False
            return True

        left = 0
        right = len(queries) + 1
        while left < right:
            middle = (left + right) // 2
            middle_array = n_queries(middle)
            if is_non_negative(middle_array):
                right = middle
            else:
                left = middle + 1
        if left > len(queries):
            return -1
        return left
