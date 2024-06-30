# level_1と同じ解法
# 余計な条件を削除
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            needed_day = 1
            current_loaded = 0
            for weight in weights:
                current_loaded += weight
                if current_loaded <= capacity:
                    continue
                needed_day += 1
                current_loaded = weight
                if needed_day > days:
                    return False
            return True

        left = max(weights)
        right = sum(weights)
        while left < right:
            middle = (left + right) // 2
            if can_ship(middle):
                right = middle
            else:
                left = middle + 1
        return left
