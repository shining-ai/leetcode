class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merge_nums = []
        index1 = 0
        index2 = 0
        while index1 < len(nums1) and index2 < len(nums2):
            id1, val1 = nums1[index1]
            id2, val2 = nums2[index2]
            if id1 == id2:
                merge_nums.append([id1, val1 + val2])
                index1 += 1
                index2 += 1
            elif id1 < id2:
                merge_nums.append([id1, val1])
                index1 += 1
            else:
                merge_nums.append([id2, val2])
                index2 += 1

        for remain in nums1[index1:]:
            merge_nums.append(remain)
        for remain in nums2[index2:]:
            merge_nums.append(remain)
        return merge_nums
