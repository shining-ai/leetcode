from heapq import heapify, heappop, heappush


def sol_1(nums1, nums2, k):
    nums1_len = len(nums1)
    nums2_len = len(nums2)
    ans = []
    heap = [(nums1[0] + nums2[0], 0, 0)]
    heapify(heap)
    seen = set()

    for _ in range(k):
        min_val, i, j = heappop(heap)
        ans.append([nums1[i], nums2[j]])

        if i + 1 < nums1_len and (i + 1, j) not in seen:
            heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            seen.add((i + 1, j))

        if j + 1 < nums2_len and (i, j + 1) not in seen:
            heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            seen.add((i, j + 1))

    return ans


def sol_2(nums1, nums2, k):
    queue = []

    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heappush(queue, [nums1[i] + nums2[j], i, j])

    push(0, 0)
    pairs = []
    while queue and len(pairs) < k:
        _, i, j = heappop(queue)
        pairs.append([nums1[i], nums2[j]])
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)
    return pairs


if __name__ == "__main__":
    nums1 = [-10, -4, 0, 0, 6]
    nums2 = [3, 5, 6, 7, 8, 100]
    k = 10

    print(sol_1(nums1, nums2, k))
    print(sol_2(nums1, nums2, k))
