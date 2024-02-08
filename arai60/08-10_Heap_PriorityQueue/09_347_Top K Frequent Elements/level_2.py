# ソートで解く
# O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return [num for num, freq in counts[:k]]


# heapqで解く
# O(nlogk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]


# quickselectで解く
# O(n) ~ O(n^2)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        counts = list(counts.items())

        def partition(left, right, pivot) -> int:
            pivot_frequency = counts[pivot][1]
            counts[pivot], counts[right] = (counts[right], counts[pivot])
            sorted_i = left
            for i in range(left, right):
                if counts[i][1] < pivot_frequency:
                    counts[sorted_i], counts[i] = counts[i], counts[sorted_i]
                    sorted_i += 1
            counts[right], counts[sorted_i] = counts[sorted_i], counts[right]
            return sorted_i

        def quickselect(left, right, kth_smallest) -> None:
            pivot = random.randint(left, right)
            pivot = partition(left, right, pivot)
            if kth_smallest == pivot:
                return
            elif kth_smallest < pivot:
                quickselect(left, pivot - 1, kth_smallest)
            else:
                quickselect(pivot + 1, right, kth_smallest)

        n = len(counts)
        quickselect(0, n - 1, n - k)
        return [num for num, freq in counts][n - k :]


# collections.Counterで解く
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        return [num for num, freq in counts.most_common(k)]
