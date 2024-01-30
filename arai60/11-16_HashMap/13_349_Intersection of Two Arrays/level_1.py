def solve_1(nums1, nums2):
    nums1_set = set(nums1)
    nums2_set = set(nums2)

    return list(nums1_set & nums2_set)


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    print(solve_1(nums1, nums2))
