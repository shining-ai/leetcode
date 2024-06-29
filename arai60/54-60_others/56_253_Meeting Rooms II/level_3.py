class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms_end_time = []
        for interval in sorted(intervals):
            start, end = interval[0], interval[1]
            for i in range(len(rooms_end_time)):
                if rooms_end_time[i] <= start:
                    rooms_end_time[i] = end
                    break
            else:
                rooms_end_time.append(end)
        return len(rooms_end_time)
