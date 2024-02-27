class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_freq = defaultdict(int)
        sum_freq[0] = 1
        subarray_num = 0
        sum = 0
        for num in nums:
            sum += num
            target = sum - k
            if target in sum_freq:
                subarray_num += sum_freq[target]
            sum_freq[sum] += 1
        return subarray_num
