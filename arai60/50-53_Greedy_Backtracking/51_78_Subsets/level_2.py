# Cascading
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = [[]]
        for num in nums:
            for current in all_subsets[:]:
                all_subsets.append(current + [num])
        return all_subsets


# bitを使った解法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        all_subsets = []
        for i in range(2**n, 2 ** (n + 1)):
            bitmask = bin(i)[3:]
            current_subset = []
            for digit in range(n):
                if bitmask[digit] == "1":
                    current_subset += [nums[digit]]
            all_subsets.append(current_subset)

        return all_subsets
