class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        min_heap = []
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        visited = set()

        def push_min_heap(index1, index2):
            if index1 < nums1_len and index2 < nums2_len:
                if (index1, index2) not in visited:
                    val = nums1[index1] + nums2[index2]
                    heapq.heappush(min_heap, (val, (index1, index2)))
                    visited.add((index1, index2))

        push_min_heap(0, 0)
        pairs = []
        while len(pairs) < k:
            _, index = heapq.heappop(min_heap)
            pairs.append([nums1[index[0]], nums2[index[1]]])
            push_min_heap(index[0] + 1, index[1])
            push_min_heap(index[0], index[1] + 1)
        return pairs
