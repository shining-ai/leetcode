# 一つ前の最小値のインデックスが(i,j)の場合、次に小さい値は(i+1,j)と(i,j+1)のどちらかである。
# これをプライオリティキューに入れていくことで、最小の値から順に取り出すことができる。
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        min_heap = [(nums1[0] + nums2[0], (0, 0))]
        visited = set()
        pairs = []
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        while len(pairs) < k:
            _, index = heapq.heappop(min_heap)
            pairs.append([nums1[index[0]], nums2[index[1]]])
            next_index_1 = (index[0] + 1, index[1])
            next_index_2 = (index[0], index[1] + 1)
            if next_index_1[0] < nums1_len:
                if next_index_1 not in visited:
                    val = nums1[next_index_1[0]] + nums2[next_index_1[1]]
                    heapq.heappush(min_heap, (val, next_index_1))
                    visited.add(next_index_1)
            if next_index_2[1] < nums2_len:
                if next_index_2 not in visited:
                    val = nums1[next_index_2[0]] + nums2[next_index_2[1]]
                    heapq.heappush(min_heap, (val, next_index_2))
                    visited.add(next_index_2)
        return pairs
