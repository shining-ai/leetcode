class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()

        @cache
        def find_max_profit(i):
            if i >= len(jobs):
                return 0
            profit_skip_i = find_max_profit(i + 1)
            next_index = bisect_left(jobs, (jobs[i][1], 0, 0), lo=i + 1)
            profit_use_i = find_max_profit(next_index) + jobs[i][2]
            return max(profit_skip_i, profit_use_i)

        return find_max_profit(0)
