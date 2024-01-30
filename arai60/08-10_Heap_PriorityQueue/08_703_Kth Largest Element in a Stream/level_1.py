import heapq
from typing import List

# 2,4,5,8
# 2,3,4,5,8
# 2,3,4,5,5,8
# 2,3,4,5,5,8,10
# 2,3,4,5,5,8,9,10
# 2,3,4,4,5,5,8,9,10


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


if __name__ == "__main__":
    k = KthLargest(3, [4, 5, 8, 2])
    print(k.add(3))
    print(k.add(5))
    print(k.add(10))
    print(k.add(9))
    print(k.add(4))
