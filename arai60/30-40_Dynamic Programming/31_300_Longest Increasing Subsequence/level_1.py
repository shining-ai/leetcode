# 単純なDP
# O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length_subsequence = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    length_subsequence[i] = max(
                        length_subsequence[j] + 1,
                        length_subsequence[i],
                    )
        return max(length_subsequence)


# インデックスの長さとなるシーケンスを作った時、最後の要素の最小値を保存していく
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        largest_subsequence = [nums[0]]
        for num in nums[1:]:
            if largest_subsequence[-1] < num:
                largest_subsequence.append(num)
            else:
                i = 0
                while largest_subsequence[i] < num:
                    i += 1
                largest_subsequence[i] = num
        return len(largest_subsequence)
