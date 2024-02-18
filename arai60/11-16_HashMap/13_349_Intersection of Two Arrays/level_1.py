# 何も見ずに解いた解放
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        intersection = []
        for num in nums1_set:
            if num in nums2:
                intersection.append(num)
        return intersection


# 解答を見てから実装
# set関数にで&演算子を使うことで共通の要素を取得できる
# https://docs.python.org/ja/3/library/stdtypes.html#set-types-set-frozenset
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set & nums2_set)
