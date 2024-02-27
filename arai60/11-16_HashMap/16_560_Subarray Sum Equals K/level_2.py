# 総当たりで探索する
# 1段目から変更なし
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sum_val = 0
            for j in range(i, len(nums)):
                sum_val += nums[j]
                if sum_val == k:
                    count += 1
        return count


# 累積和を使って全探索する
# 累積和の変数名を変更
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_sums = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            num_sums[i + 1] = num_sums[i] + num
        count = 0
        for i, start in enumerate(num_sums):
            for end in num_sums[i + 1 :]:
                if end - start == k:
                    count += 1
        return count


# 累積和をハッシュマップに保存して探索する
# 変数targetを作成し、探しているものを明確にした
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_freq = defaultdict(int)
        count = 0
        sum_val = 0
        for num in nums:
            sum_freq[sum_val] += 1
            sum_val += num
            target = sum_val - k
            count += sum_freq[target]
        return count
