# O(nlogn)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_num = 1
        for num in sorted(nums):
            if num <= 0:
                continue
            if min_num < num:
                return min_num
            min_num = num + 1
        return min_num


# O(n)
# 出てきた数字をメモしておいて、0から順番に見ていく
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen_num = [False] * (len(nums) + 2)
        for num in nums:
            if num <= 0 or len(nums) < num:
                continue
            seen_num[num] = True
        seen_num[0] = True
        for i, has_num in enumerate(seen_num):
            if not has_num:
                return i

