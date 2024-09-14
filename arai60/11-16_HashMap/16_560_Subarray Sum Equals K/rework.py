# 総当たりで解く(TLE)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            current = 0
            for end in range(start, len(nums)):
                current += nums[end]
                if current == k:
                    count += 1
        return count


# 累積和を使って全探索する(TLE)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_cumulative = [0]
        for num in nums:
            nums_cumulative.append(num + nums_cumulative[-1])
        count = 0
        for start in range(len(nums_cumulative)):
            for end in range(start + 1, len(nums_cumulative)):
                if nums_cumulative[end] - nums_cumulative[start] == k:
                    count += 1
        return count


# 累積和をハッシュマップに保存して探索する
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_cumulative = [0]
        for num in nums:
            nums_cumulative.append(num + nums_cumulative[-1])
        targets = defaultdict(int)
        count = 0
        for num_cumulative in nums_cumulative:
            count += targets[num_cumulative]
            targets[k + num_cumulative] += 1
        return count
