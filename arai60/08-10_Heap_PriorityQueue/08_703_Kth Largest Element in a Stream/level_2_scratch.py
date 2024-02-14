class PriorityQueue:
    def __init__(self, nums: List[int]):
        self.heap = []
        for num in nums:
            self.push(num)

    def __parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def __left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def __right_child_index(self, index: int) -> int:
        return 2 * index + 2

    def __has_child(self, index: int) -> bool:
        return self.__left_child_index(index) < len(self.heap)

    def __has_right_child(self, index: int) -> bool:
        return self.__right_child_index(index) < len(self.heap)

    def __smaller_child(self, index: int) -> int:
        smaller_chiled_index = self.__left_child_index(index)
        if (
            self.__has_right_child(index)
            and self.heap[self.__right_child_index(index)]
            < self.heap[smaller_chiled_index]
        ):
            smaller_chiled_index = self.__right_child_index(index)
        return smaller_chiled_index

    def push(self, val: int):
        added_index = len(self.heap)
        self.heap.append(val)
        while added_index > 0:
            parent_index = self.__parent_index(added_index)
            if self.heap[added_index] > self.heap[parent_index]:
                break
            self.heap[added_index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[added_index],
            )
            added_index = parent_index

    def pop(self) -> int:
        smallest = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        added_index = 0
        while self.__has_child(added_index):
            smaller_child_index = self.__smaller_child(added_index)
            if self.heap[added_index] < self.heap[smaller_child_index]:
                break
            self.heap[added_index], self.heap[smaller_child_index] = (
                self.heap[smaller_child_index],
                self.heap[added_index],
            )
            added_index = smaller_child_index
        return smallest


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.priority_queue = PriorityQueue([])
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.priority_queue.push(val)
        if len(self.priority_queue.heap) > self.k:
            self.priority_queue.pop()
        return self.priority_queue.heap[0]
