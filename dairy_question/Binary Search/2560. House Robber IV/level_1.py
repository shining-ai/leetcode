class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def count_under_value(value):
            num_rob = 0
            i = 0
            while i < len(nums):
                if nums[i] <= value:
                    num_rob += 1
                    i += 1
                i += 1
            return num_rob

        left = 0
        right = max(nums)
        while left < right:
            middle = (left + right) // 2
            if k <= count_under_value(middle):
                right = middle
            else:
                left = middle + 1
        return left
