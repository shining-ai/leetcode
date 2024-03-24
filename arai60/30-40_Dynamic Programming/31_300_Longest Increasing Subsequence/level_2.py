# 単純なDP
# level1の解法と同じ
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # インデックスが最後の要素となるシーケンスの最大長
        length_subsequence = [1] * len(nums)

        def calc_length_subsequence(end):
            max_length = 1
            for i in range(end):
                if nums[i] < nums[end]:
                    max_length = max(length_subsequence[i] + 1, max_length)
            return max_length

        for i in range(len(nums)):
            length_subsequence[i] = calc_length_subsequence(i)
        return max(length_subsequence)


# 部分列を作成する
# 部分列は最小の要素で構成する
# 二分探索を使い高速化
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # インデックスの長さとなるシーケンスを作った時、最後の要素の最小値
        min_last_element_subsequence = []
        for num in nums:
            # numが最後の要素となるシーケンスの最大長
            length_subsequence = bisect_left(min_last_element_subsequence, num)
            if length_subsequence >= len(min_last_element_subsequence):
                min_last_element_subsequence.append(num)
            else:
                min_last_element_subsequence[length_subsequence] = num
        return len(min_last_element_subsequence)


# セグメントツリーを使用
# 座標圧縮も行う
class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (2 * size)

    def update(self, index, value):
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
        def compress(arr):
            sorted_arr = sorted(arr)
            val_to_index = {}
            for i, val in enumerate(sorted_arr):
                val_to_index[val] = i
            compressed_arr = [val_to_index[val] for val in arr]
            return compressed_arr

        nums = compress(nums)
        segment_tree = SegmentTree(len(nums))
        for num in nums:
            length_subsequence = segment_tree.query(0, num)
            segment_tree.update(num, length_subsequence + 1)
        return segment_tree.query(0, len(nums))


# BITを使用
# 座標圧縮も行う
class BIT:
    def __init__(self, nums):
        self.bit_size = len(nums) + 1
        self.bit = [0] * (self.bit_size)

    def update(self, index, value):
        while index < self.bit_size:
            self.bit[index] = max(self.bit[index], value)
            index += index & -index

    def query(self, index):
        # 開区間[0, index] の範囲の最大値を返す
        max_value = 0
        while 0 < index:
            max_value = max(self.bit[index], max_value)
            index -= index & -index
        return max_value


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def compress(arr):
            sorted_arr = sorted(arr)
            val_to_index = {}
            for i, val in enumerate(sorted_arr):
                val_to_index[val] = i + 1  # BITのため最小値は1にする
            compressed_arr = [val_to_index[val] for val in arr]
            return compressed_arr

        compress_nums = compress(nums)
        bit = BIT(compress_nums)
        for num in compress_nums:
            length_subsequence = bit.query(num - 1)
            bit.update(num, length_subsequence + 1)
        return bit.query(len(compress_nums))
