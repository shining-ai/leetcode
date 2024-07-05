# 1段目から特に変更なし
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        intersection = []
        for num in nums1_set:
            if num in nums2:
                intersection.append(num)
        return intersection


# setに&えn演算子を使う方法
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
            assert nums1_sorted[i] == nums2_sorted[j]
            # nums1とnums2の等しい要素に対する処理
            latest_intersection = nums1_sorted[i]
            intersection.append(latest_intersection)
            while i < len(nums1) and nums1_sorted[i] == latest_intersection:
                i += 1
            while j < len(nums2) and nums2_sorted[j] == latest_intersection:
                j += 1
        return intersection


# 辞書を使う方法
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = defaultdict(bool)
        for num1 in nums1:
            seen[num1] = True

        intersections = []
        for num2 in nums2:
            if seen[num2]:
                intersections.append(num2)
                seen[num2] = False
        return intersections
