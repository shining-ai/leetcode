# DP
# i番目以降のjobを使った時の最大利益をメモしていく
class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        max_profit_begin_i = [None] * len(jobs)
        max_profit_begin_i.append(0)

        def find_max_profit(i):
            if max_profit_begin_i[i] is not None:
                return max_profit_begin_i[i]
            profit_skip_i = find_max_profit(i + 1)
            next_index = bisect.bisect_left(jobs, (jobs[i][1], 0, 0), lo=i + 1)
            profit_use_i = find_max_profit(next_index) + jobs[i][2]
            max_profit_begin_i[i] = max(profit_skip_i, profit_use_i)
            return max_profit_begin_i[i]

        return find_max_profit(0)
