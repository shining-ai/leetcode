class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def possible_rob(value):
            num_rob = 0
            i = 0
            while i < len(nums):
                if nums[i] <= value:
                    num_rob += 1
                    i += 1
                i += 1
            return k <= num_rob

        left = 0
        right = max(nums)
        while left < right:
            middle = (left + right) // 2
            if possible_rob(middle):
                right = middle
            else:
                left = middle + 1
        return left
