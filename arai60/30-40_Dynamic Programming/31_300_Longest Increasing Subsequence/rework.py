# No.1 全探索
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence_length_until = [1] * len(nums)
        for end in range(1, len(nums)):
            for i in range(end):
                if nums[i] >= nums[end]:
                    continue
                subsequence_length_until[end] = max(
                    subsequence_length_until[end],
                    subsequence_length_until[i] + 1,
                )
        return max(subsequence_length_until)


# No.2 subsequenceを作成する
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]
        for num in nums[1:]:
            if subsequence[-1] < num:
                subsequence.append(num)
                continue
            i = 0
            while subsequence[i] < num:
                i += 1
            subsequence[i] = num
        return len(subsequence)


# No.3 No.2に2分探索を使って高速化
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]
        for num in nums[1:]:
            if subsequence[-1] < num:
                subsequence.append(num)
                continue
            i = bisect_left(subsequence, num)
            subsequence[i] = num
        return len(subsequence)


# No.3 subsequenceの長さがiのとき、最後の要素が最小のものを記録しておく
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        min_val_sequence = []
        for num in nums:
            # numが最後の要素となるシーケンスの長さ
            sequence_length = bisect_left(min_val_sequence, num)
            if len(min_val_sequence) <= sequence_length:
                min_val_sequence.append(num)
            else:
                min_val_sequence[sequence_length] = num
        return len(min_val_sequence)


# No.4 セグメントツリーを使用
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
