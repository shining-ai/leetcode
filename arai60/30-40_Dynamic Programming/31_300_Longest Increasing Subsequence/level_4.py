# level_1の書き換え
# 単純なDP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # インデックスが最後の要素となるシーケンスの最大長
        subsequence_length_using_index_as_last = [1] * len(nums)
        for current_index in range(len(nums)):
            for past_index in range(current_index):
                if nums[past_index] < nums[current_index]:
                    subsequence_length_using_index_as_last[current_index] = (
                        max(
                            subsequence_length_using_index_as_last[past_index]
                            + 1,
                            subsequence_length_using_index_as_last[
                                current_index
                            ],
                        )
                    )
        return max(subsequence_length_using_index_as_last)


# level_2 セグメントツリーの書き換え
class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (2 * size)

    def update(self, index, value):
        # 同じindexに複数回updateされることは想定していない
        index += self.size
        self.tree[index] = value
        while index > 0:
            index //= 2
            self.tree[index] = max(self.tree[index], value)

    def query(self, left, right):
        # [left, right) の範囲の最大値を返す
        left += self.size
        right += self.size
        max_value = 0
        while left < right:
            if left % 2 == 1:
                max_value = max(max_value, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1  # 閉区間のため1つ前の要素を確認
                max_value = max(max_value, self.tree[right])
            left //= 2
            right //= 2
        return max_value


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def compress(nums):
            sorted_nums = sorted(nums)
            val_to_index = {}
            for i, val in enumerate(sorted_nums):
                val_to_index[val] = i
            compressed_nums = [val_to_index[val] for val in nums]
            return compressed_nums

        nums = compress(nums)
        segment_tree = SegmentTree(len(nums))
        for num in nums:
            length_subsequence = segment_tree.query(0, num)
            segment_tree.update(num, length_subsequence + 1)
        return segment_tree.query(0, len(nums))
