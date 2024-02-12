# 同じような処理をしていたので関数化
# kが大きいと無限ループになるので、一応whileの条件にmin_heapを追加した
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        min_heap = []
        visited = set()
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        def push_min_heap(nums1_index, nums2_index):
            if nums1_index < nums1_len and nums2_index < nums2_len:
                if (nums1_index, nums2_index) not in visited:
                    val = nums1[nums1_index] + nums2[nums2_index]
                    heapq.heappush(min_heap, (val, (nums1_index, nums2_index)))
                    visited.add((nums1_index, nums2_index))

        push_min_heap(0, 0)
        pairs = []
        while len(pairs) < k and min_heap:
            _, index = heapq.heappop(min_heap)
            pairs.append([nums1[index[0]], nums2[index[1]]])
            push_min_heap(index[0] + 1, index[1])
            push_min_heap(index[0], index[1] + 1)
        return pairs


# 重複チェックなしでheapに追加する
# あまり直感的ではない
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        min_heap = []

        def push_min_heap(nums1_index, nums2_index):
            if nums1_index < len(nums1) and nums2_index < len(nums2):
                val = nums1[nums1_index] + nums2[nums2_index]
                heapq.heappush(min_heap, (val, (nums1_index, nums2_index)))

        push_min_heap(0, 0)
        pairs = []
        while min_heap and len(pairs) < k:
            _, index = heappop(min_heap)
            pairs.append([nums1[index[0]], nums2[index[1]]])
            push_min_heap(index[0], index[1] + 1)
            if index[1] == 0:
                push_min_heap(index[0] + 1, 0)
        return pairs
