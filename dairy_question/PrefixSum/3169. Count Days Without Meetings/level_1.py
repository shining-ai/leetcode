# 素直に実装(TLE)
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        available_day = [True] * (days + 1)
        for start_day, end_day in meetings:
            for i in range(start_day, end_day + 1):
                available_day[i] = False

        num_free = -1  # 0-indexed
        for i in available_day:
            if i:
                num_free += 1
        return num_free


# 累積和を使って解く(OOM)
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        prefix_sum = 0
        different_map = [0] * (days + 1)

        for start_day, end_day in meetings:
            different_map[start_day] += 1
            if end_day >= days:
                continue
            different_map[end_day + 1] -= 1

        prefix_sum = 0
        free_day = 0
        for i in different_map[1:]:
            prefix_sum += i
            if prefix_sum == 0:
                free_day += 1
        return free_day


# ソートして解く
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev_end = 0
        available_day = 0
        for start_day, end_day in meetings:
            if prev_end < start_day:
                available_day += start_day - prev_end - 1
            prev_end = max(prev_end, end_day)
        available_day += days - prev_end
        return available_day
