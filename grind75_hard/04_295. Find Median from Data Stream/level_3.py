class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        index = bisect_left(self.nums, num)
        self.nums.insert(index, num)

    def findMedian(self) -> float:
        if len(self.nums) % 2:
            return float(self.nums[len(self.nums) // 2])
        else:
            high_index = len(self.nums) // 2
            low_index = high_index - 1
            return (self.nums[high_index] + self.nums[low_index]) / 2
