# heapに入れて最小値を取得していく
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        min_heap = [(0, (0, 0))]
        seen = set()
        pairs = []

        def min_heap_push(index_1, index_2):
            if not (0 <= index_1 < len(nums1)):
                return
            if not (0 <= index_2 < len(nums2)):
                return
            val = nums1[index_1] + nums2[index_2]
            heappush(min_heap, (val, (index_1, index_2)))

        while len(pairs) < k and min_heap:
            val, index = heappop(min_heap)
            if index in seen:
                continue
            pairs.append([nums1[index[0]], nums2[index[1]]])
            seen.add(index)
            min_heap_push(index[0] + 1, index[1])
            min_heap_push(index[0], index[1] + 1)

        return pairs
