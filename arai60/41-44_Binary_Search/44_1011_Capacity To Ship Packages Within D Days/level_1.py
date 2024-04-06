# 解答と同様の実装
# 運べるかどうかを試して、capacityを2分探索する
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_shipp(capacity):
            needed_day = 1
            current_loaded = 0
            for weight in weights:
                if capacity < weight:
                    return False
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
            if can_shipp(middle):
                right = middle
            else:
                left = middle + 1
        return left
