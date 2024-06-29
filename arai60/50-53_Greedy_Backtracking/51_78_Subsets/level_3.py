class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def make_subset(begin, current, subset_length):
            if len(current) == subset_length:
                all_subsets.append(current[:])
                return
            for i in range(begin, len(nums)):
                current.append(nums[i])
                make_subset(i + 1, current, subset_length)
                current.pop()

        all_subsets = []
        for i in range(len(nums) + 1):
            make_subset(0, [], i)
        return all_subsets
