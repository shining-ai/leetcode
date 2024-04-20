# 開始と終了を時系列に調べていく
# 開始時刻になったら会議を増やし、終了時刻になったら会議数を減らせば、開かれている会議数が分かる
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = []
        for interval in intervals:
            sorted_intervals.append((interval[0], "start"))
            sorted_intervals.append((interval[1], "end"))
        sorted_intervals.sort()
        max_rooms = 0
        rooms = 0
        for _, time_type in sorted_intervals:
            if time_type == "start":
                rooms += 1
                max_rooms = max(max_rooms, rooms)
            else:
                rooms -= 1
        return max_rooms
