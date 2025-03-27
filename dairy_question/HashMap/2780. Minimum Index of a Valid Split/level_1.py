class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count_num = defaultdict(int)
        for num in nums:
            count_num[num] += 1
        max_freq = (0, 0)
        current_freq = defaultdict(int)
        for i, num in enumerate(nums):
            current_freq[num] += 1
            if current_freq[num] <= max_freq[0]:
                continue
            max_freq = (current_freq[num], num)
            if (i + 1) < current_freq[num] * 2:
                if len(nums) - i - 1 < (count_num[num] - current_freq[num]) * 2:
                    return i
        return -1
