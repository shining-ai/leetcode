# ソートをheapqで代替
# 元のリストは破壊される
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        heapq.heapify(intervals)
        previous_end = 0
        while intervals:
            start, end = heapq.heappop(intervals)
            if previous_end > start:
                return False
            previous_end = end
        return True
