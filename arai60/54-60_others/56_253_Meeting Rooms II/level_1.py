# 会議室を作成して最後にカウントする
# 会議室の利用終了時間を格納しておき、新しい会議が始まる時間と比較して、会議室を使い回す
# 使い回せない場合は新しい会議室を作成する
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
