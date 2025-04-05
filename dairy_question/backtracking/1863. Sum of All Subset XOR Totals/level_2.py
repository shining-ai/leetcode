class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def helper(index, current):
            if index == len(nums):
                return current

            without_element = helper(index + 1, current)
            with_element = helper(index + 1, current ^ nums[index])
            return without_element + with_element
        return helper(0, 0)
