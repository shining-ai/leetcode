class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        previous_end = 0
        for interval in sorted(intervals):
            start, end = interval[0], interval[1]
            if previous_end > start:
                return False
            previous_end = end
        return True
