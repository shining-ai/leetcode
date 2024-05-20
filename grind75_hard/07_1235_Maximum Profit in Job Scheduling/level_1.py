# startTimeでソートして、繋げられるものを順番に確認していく
# 終了時刻の早いものから見ていき、最大の利益になるものを選択していく
# (最大の利益にならないものは、それ以降でも最大にならないため捨てて良い)
# 例:(start, end, profit) = ((1, 3 50), (2, 3, 10), (3, 5, 40), (4, 6, 70))
# 3項目の選択肢は
# (1, 3, 50) -> (3, 5, 40)の順番で選択すると最大の利益になる
# (2, 3, 10) -> (3, 5, 40)は最大の利益にならない(4項目以降でも最大の利益にならないので捨てる)
# 4項目の選択肢は
# (1, 3, 50) -> (4, 6, 70)の順番で選択すると最大の利益になる
# (2, 3, 10)は3項目の検討時に捨てた
class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        sorted_starts = sorted([(startTime[i], i) for i in range(len(startTime))])
        max_profit = 0
        end_profit_heap = [(0, 0)]
        for start, i in sorted_starts:
            max_profit_use_i = 0
            pre_info = ()
            while end_profit_heap and end_profit_heap[0][0] <= start:
                pre_end, pre_profit = heapq.heappop(end_profit_heap)
                if pre_profit + profit[i] <= max_profit_use_i:
                    continue
                max_profit_use_i = pre_profit + profit[i]
                pre_info = (pre_end, pre_profit)
            heapq.heappush(end_profit_heap, (endTime[i], max_profit_use_i))
            max_profit = max(max_profit, max_profit_use_i)
            if pre_info:
                heapq.heappush(end_profit_heap, pre_info)
        return max_profit
