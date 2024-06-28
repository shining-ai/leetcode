class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_val = -math.inf
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num[0], i, 0))
            max_val = max(max_val, num[0])

        smallest_range = math.inf
        while 1:
            min_val, i, index = heapq.heappop(min_heap)
            if max_val - min_val < smallest_range:
                smallest_range = max_val - min_val
                ans = [min_val, max_val]
            if index + 1 >= len(nums[i]):
                break
            heapq.heappush(min_heap, (nums[i][index + 1], i, index + 1))
            max_val = max(max_val, nums[i][index + 1])
        return ans
