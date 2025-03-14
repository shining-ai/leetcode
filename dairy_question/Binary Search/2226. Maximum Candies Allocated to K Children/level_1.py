class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_allocate(num_allocate):
            if num_allocate == 0:
                return True
            can_get_child = 0
            for candy in candies:
                can_get_child += candy // num_allocate
                if can_get_child >= k:
                    return True
            return False

        left = 0
        right = max(candies)
        while left < right:
            middle = (left + right + 1) // 2
            if can_allocate(middle):
                left = middle
            else:
                right = middle - 1
        return right
