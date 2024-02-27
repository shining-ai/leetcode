# 解答を見て実装
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calc_day(capacity):
            loaded = 0
            needed_day = 1
            for weight in weights:
                loaded += weight
                if loaded > capacity:
                    needed_day += 1
                    loaded = weight
            return needed_day

        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            needed_day = calc_day(mid)
            if days < needed_day:
                left = mid + 1
            else:
                right = mid

        return left
