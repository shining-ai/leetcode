class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        last_nonzero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[last_nonzero + 1] = nums[i]
            last_nonzero += 1

        for i in range(last_nonzero + 1, len(nums)):
            nums[i] = 0
        return nums
