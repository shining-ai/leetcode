class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms_end_time = []
        for interval in sorted(intervals):
            start, end = interval[0], interval[1]
            if rooms_end_time and rooms_end_time[0] <= start:
                heapq.heappop(rooms_end_time)
            heapq.heappush(rooms_end_time, end)
        return len(rooms_end_time)
