# モジュールを使用
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for i in range(len(nums) + 1):
            subsets.extend(itertools.combinations(nums, i))
        return [list(subset) for subset in subsets]


# Backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def make_subset(begin, current, subset_length):
            if len(current) == subset_length:
                subsets.append(current[:])
                return
            for i in range(begin, len(nums)):
                current.append(nums[i])
                make_subset(i + 1, current, subset_length)
                current.pop()

        subsets = []
        for i in range(len(nums) + 1):
            make_subset(0, [], i)
        return subsets
