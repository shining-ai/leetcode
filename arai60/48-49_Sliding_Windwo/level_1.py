# ポインターを2つ使って、最小の長さを求める
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = math.inf
        left = 0
        sum_subarray = 0
        for right, num in enumerate(nums):
            sum_subarray += num
            while target <= sum_subarray:
                min_length = min(min_length, right - left + 1)
                sum_subarray -= nums[left]
                left += 1
        if min_length == math.inf:
            return 0
        return min_length


# 累積和を使用した解法
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cumurative_sums = [0]
        min_length = math.inf
        left = 0
        for num in nums:
            cumurative_sums.append(cumurative_sums[-1] + num)
        for right in range(len(cumurative_sums)):
            while left < right:
                if cumurative_sums[right] - cumurative_sums[left] < target:
                    break
                min_length = min(min_length, right - left)
                left += 1
        if min_length == math.inf:
            return 0
        return min_length
