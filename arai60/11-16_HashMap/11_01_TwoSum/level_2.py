# 総当たりで判定
# for文はrangeを使う方法に統一
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]


# hash mapを使って判定
# (target - num)を変数に格納
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_to_index = {}
        for i, num in enumerate(nums):
            number_to_index[num] = i
        for i, num in enumerate(nums):
            difference = target - num
            if difference not in number_to_index:
                continue
            if number_to_index[difference] == i:
                continue
            return [i, number_to_index[difference]]


# One-pass Hash Table
# hash mapにあればreturnするように素直に書き換え
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_to_index = {}
        for i, num in enumerate(nums):
            if num in number_to_index:
                return [number_to_index[num], i]
            number_to_index[target - num] = i


# ソートして頭と尾から探索
# コメントを見て実装
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)

        def original_indexes(left, right):
            orig_left = nums.index(sorted_nums[left])
            orig_right = nums.index(sorted_nums[right])
            if orig_left == orig_right:
                orig_right = nums.index(sorted_nums[right], orig_left + 1)
            return [orig_left, orig_right]

        left = 0
        right = len(nums) - 1
        while left < right:
            pair_sum = sorted_nums[left] + sorted_nums[right]
            if pair_sum == target:
                return original_indexes(left, right)
            if pair_sum < target:
                left += 1
            if pair_sum > target:
                right -= 1
        return []
