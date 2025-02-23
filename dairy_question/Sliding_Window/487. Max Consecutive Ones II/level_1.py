class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        last_zero = -1
        last2_zero = -1
        max_length = 0
        for i, num in enumerate(nums):
            if num == 0:
                last2_zero = last_zero
                last_zero = i
            max_length = max(max_length, i - last2_zero)

        return max_length
