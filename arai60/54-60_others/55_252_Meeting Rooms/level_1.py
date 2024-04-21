# 予定のある時間を全て記憶していく
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        scheduled = set()
        for interval in intervals:
            start, end = interval[0], interval[1]
            for i in range(start, end):
                if i in scheduled:
                    return False
                scheduled.add(i)
        return True


# ソートして前の予定の終了時間と次の予定の開始時間を比較する
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        previous_end = 0
        for interval in sorted(intervals):
            start, end = interval[0], interval[1]
            if previous_end > start:
                return False
            previous_end = end
        return True
