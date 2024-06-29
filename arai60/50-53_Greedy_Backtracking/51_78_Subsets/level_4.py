# Backtracking
# subsetの長さの指定を不要にした。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def make_subset(begin, current):
            if len(current) > len(nums):
                return
            subsets.append(current[:])
            for i in range(begin, len(nums)):
                current.append(nums[i])
                make_subset(i + 1, current)
                current.pop()

        subsets = []
        make_subset(0, [])
        return subsets
