# モジュールを使用
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums, len(nums)))


# バックトラッキング
# 解答を見て実装
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def make_permutations(current):
            if len(current) == len(nums):
                permutations.append(current[:])
                return
            for num in nums:
                if num in current:
                    continue
                current.append(num)
                make_permutations(current)
                current.pop()

        permutations = []
        make_permutations([])
        return permutations
