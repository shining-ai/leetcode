# DP
class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = list(sorted(zip(startTime, endTime, profit)))
        max_profit = [0] * (len(jobs) + 1)
        for i in range(len(jobs) - 1, -1, -1):
            profit_skip_running_job = max_profit[i + 1]
            next_index = bisect_left(jobs, (jobs[i][1], 0, 0), lo=i + 1)
            profit_use_running_job = max_profit[next_index] + jobs[i][2]
            max_profit[i] = max(profit_skip_running_job, profit_use_running_job)
        return max_profit[0]


# level_1の書き直し
class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = list(sorted(zip(startTime, endTime, profit)))
        jobs.append((float("inf"), float("inf"), 0))
        max_profit = 0
        running_jobs = []
        for job_start, job_end, job_profit in jobs:
            while running_jobs and running_jobs[0][0] <= job_start:
                _, max_profit_from_running_job = heapq.heappop(running_jobs)
                max_profit = max(max_profit, max_profit_from_running_job)
            heapq.heappush(running_jobs, (job_end, max_profit + job_profit))
        return max_profit
