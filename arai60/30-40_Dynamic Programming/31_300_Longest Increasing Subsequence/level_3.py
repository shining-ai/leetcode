# level_2の2番目の回答
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = []
        for num in nums:
            length_sequence = bisect_left(subsequence, num)
            if length_sequence >= len(subsequence):
                subsequence.append(num)
            else:
                subsequence[length_sequence] = num
        return len(subsequence)
