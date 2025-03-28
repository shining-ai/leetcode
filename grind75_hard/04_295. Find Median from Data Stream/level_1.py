# 毎回ソートする
# TimeOut
class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        if len(self.nums) % 2:
            index = len(self.nums) // 2
            return float(self.nums[index])

        else:
            index = len(self.nums) // 2
            return (self.nums[index - 1] + self.nums[index]) / 2


# heapを2つ使う
# 半分より大きい値をいれるheapと小さい値をいれるheapの2種類を使って真ん中の値を取得する
class MedianFinder:

    def __init__(self):
        self.low_heap = []
        self.high_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.high_heap, num)
        high_min = heapq.heappop(self.high_heap)
        heapq.heappush(self.low_heap, -high_min)  # low_heapは降順にしたいので-1をかける
        if len(self.high_heap) < len(self.low_heap):
            low_max = -heapq.heappop(self.low_heap)
            heapq.heappush(self.high_heap, low_max)

    def findMedian(self) -> float:
        if (len(self.high_heap) + len(self.low_heap)) % 2:
            return float(self.high_heap[0])
        else:
            middle_low = -self.low_heap[0]
            middle_high = self.high_heap[0]
            return (middle_low + middle_high) / 2
