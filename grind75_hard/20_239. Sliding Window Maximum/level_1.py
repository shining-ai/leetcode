class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        maxes = []
        for i in range(len(nums)):
            if window and window[0] < i - k + 1:
                window.popleft()
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)
            if i < k - 1:
                continue
            maxes.append(nums[window[0]])
        return maxes
