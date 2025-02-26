class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_absolute_sum = 0
        current_plus = 0
        current_minus = 0
        for num in nums:
            current_plus += num
            current_minus -= num
            if current_plus < 0:
                current_plus = 0
            if current_minus < 0:
                current_minus = 0
            max_absolute_sum = max(max_absolute_sum, current_plus)
            max_absolute_sum = max(max_absolute_sum, current_minus)
        
        return max_absolute_sum
        


        