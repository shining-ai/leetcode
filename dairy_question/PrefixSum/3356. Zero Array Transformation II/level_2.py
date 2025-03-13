# numsの要素ごとに累積和を使ったクエリを適用
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        difference_array = [0] * (len(nums) + 1)
        num_query = 0
        current_sum = 0
        for index in range(len(nums)):
            while current_sum + difference_array[index] < nums[index]:
                if num_query >= len(queries):
                    return -1
                l, r, val = queries[num_query]
                if index <= r:
                    difference_array[max(l, index)] += val
                    difference_array[r + 1] -= val
                num_query += 1
            current_sum += difference_array[index]
            index += 1
        return num_query
