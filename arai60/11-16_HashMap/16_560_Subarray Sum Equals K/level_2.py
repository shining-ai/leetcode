# 総当たりで探索する
# 1段目から変更なし
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


# 累積和を使って全探索する
# 累積和の変数名を変更
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_sums = [0]
        for i, num in enumerate(nums):
            num_sums.append(num_sums[i] + num)
        subarray_num = 0
        for i, start in enumerate(num_sums):
            for end in num_sums[i + 1 :]:
                if end - start == k:
                    subarray_num += 1
        return subarray_num


# 累積和をハッシュマップに保存して探索する
# 変数targetを作成し、探しているものを明確にした
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_freq = defaultdict(int)
        sum_freq[0] = 1
        subarray_num = 0
        sum = 0
        for num in nums:
            sum += num
            target = sum - k
            subarray_num += sum_freq[target]
            sum_freq[sum] += 1
        return subarray_num
