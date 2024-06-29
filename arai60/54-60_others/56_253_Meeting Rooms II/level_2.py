# 開始と終了を時系列に調べていく
# 開始時刻になったら会議を増やし、終了時刻になったら会議数を減らせば、開かれている会議数が分かる
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        def sort_events(intervals):
            sorted_events = []
            for interval in intervals:
                sorted_events.append((interval[0], "start"))
                sorted_events.append((interval[1], "end"))
            return sorted(sorted_events)

        sorted_events = sort_events(intervals)
        max_rooms = 0
        rooms = 0
        for _, event_type in sorted_events:
            if event_type == "start":
                rooms += 1
                max_rooms = max(max_rooms, rooms)
            else:
                rooms -= 1
        return max_rooms
