# 1段目から特に変更なし
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        intersection = []
        for num in nums1_set:
            if num in nums2:
                intersection.append(num)
        return intersection


# 1段目から特に変更なし
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set & nums2_set)


# sortする方法もあるというコメントを見て実装
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_sorted = sorted(nums1)
        nums2_sorted = sorted(nums2)
        intersection = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1_sorted[i] < nums2_sorted[j]:
                i += 1
                continue
            if nums1_sorted[i] > nums2_sorted[j]:
                j += 1
                continue
            if nums1_sorted[i] not in intersection:
                intersection.append(nums1_sorted[i])
            i += 1
            j += 1
        return intersection
