class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_kth_small(k, nums1, nums2):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]
            middle_1 = len(nums1) // 2
            middle_2 = len(nums2) // 2
            if middle_1 + middle_2 < k:
                if nums1[middle_1] < nums2[middle_2]:
                    return get_kth_small(k - middle_1 - 1, nums1[middle_1 + 1 :], nums2)
                return get_kth_small(k - middle_2 - 1, nums1, nums2[middle_2 + 1 :])
            if nums1[middle_1] < nums2[middle_2]:
                return get_kth_small(k, nums1, nums2[:middle_2])
            return get_kth_small(k, nums1[:middle_1], nums2)

        nums_length = len(nums1) + len(nums2)
        if nums_length % 2 == 1:
            return get_kth_small(nums_length // 2, nums1, nums2)
        return (
            get_kth_small(nums_length // 2 - 1, nums1, nums2)
            + get_kth_small(nums_length // 2, nums1, nums2)
        ) / 2
