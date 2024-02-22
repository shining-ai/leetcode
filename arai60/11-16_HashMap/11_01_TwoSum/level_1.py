# 総当たりで判定
# O(n!)の計算量
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if target == num + nums[j]:
                    return [i, j]


# hash mapを使って判定
# hash mapのカテゴリにあったから気づけた
# O(n)の計算量
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            hash_map[num] = i
        for i, num in enumerate(nums):
            if (target - num) not in hash_map:
                continue
            if hash_map[(target - num)] == i:
                continue
            return [i, hash_map[(target - num)]]


# One-pass Hash Table
# 解答を見た
# O(n)の計算量
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if num not in hash_map:
                hash_map[target - num] = i
                continue
            return [hash_map[num], i]
