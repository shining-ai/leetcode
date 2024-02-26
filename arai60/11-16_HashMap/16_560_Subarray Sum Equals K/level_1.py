# 総当たりで探索する(TLE)
# O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_num = 0
        for i in range(len(nums)):
            sum = 0
            for num in nums[i:]:
                sum += num
                if sum == k:
                    subarray_num += 1
        return subarray_num


# 累積和を使って全探索する(TLE)
# O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = [0]
        for i, num in enumerate(nums):
            cumulative_sum.append(cumulative_sum[i] + num)
        subarray_num = 0
        for i, start in enumerate(cumulative_sum):
            for end in cumulative_sum[i + 1 :]:
                if end - start == k:
                    subarray_num += 1
        return subarray_num


# 解答を見て作成
# 累積和をハッシュマップに保存して探索する
# O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = defaultdict(int)
        cumulative_sum[0] = 1
        subarray_num = 0
        sum = 0
        for num in nums:
            sum += num
            subarray_num += cumulative_sum[sum - k]
            cumulative_sum[sum] += 1
        return subarray_num
