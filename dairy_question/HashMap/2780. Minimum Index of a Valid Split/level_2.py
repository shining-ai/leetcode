# HashMapを2つ使って前後から数える
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count_from_tail = defaultdict(int)
        for num in nums:
            count_from_tail[num] += 1
        count_from_head = defaultdict(int)
        for index, num in enumerate(nums):
            count_from_head[num] += 1
            count_from_tail[num] -= 1
            if count_from_head[num] * 2 <= index + 1:
                continue
            if count_from_tail[num] * 2 <= len(nums) - index - 1:
                continue
            return index
        return -1

