"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        min_heap = []
        for parson in schedule:
            for time in parson:
                heapq.heappush(min_heap, (time.start, time.end))

        free_time = []
        until = -math.inf

        while min_heap:
            start, end = heapq.heappop(min_heap)
            if until != -math.inf and until < start:
                free_time.append(Interval(until, start))
            until = max(until, end)
        return free_time
