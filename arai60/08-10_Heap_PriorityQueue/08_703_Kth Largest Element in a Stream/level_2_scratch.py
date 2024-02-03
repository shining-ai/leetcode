def _swap_child(nums: List[int], parent_pos: int):
    end_pos = len(nums)
    child_pos = 2 * parent_pos + 1  # left child
    if child_pos >= end_pos:
        return None
    right_child_pos = child_pos + 1
    if right_child_pos < end_pos and nums[right_child_pos] < nums[child_pos]:
        child_pos = right_child_pos
    if nums[child_pos] < nums[parent_pos]:
        nums[parent_pos], nums[child_pos] = nums[child_pos], nums[parent_pos]
        return child_pos
    return None


def make_priority_queue(nums: List[int]):
    end_pos = len(nums)
    for parent_pos in reversed(range(end_pos // 2)):
        swap_pos = _swap_child(nums, parent_pos)
        while swap_pos is not None:
            swap_pos = _swap_child(nums, swap_pos)
    return nums


def push_priority_queue(nums: List[int], val: int):
    nums.append(val)
    pos = len(nums) - 1
    while pos > 0:
        parent_pos = (pos - 1) // 2
        if nums[pos] < nums[parent_pos]:
            nums[parent_pos], nums[pos] = nums[pos], nums[parent_pos]
            pos = parent_pos
            continue
        break
    return nums


def pop_priority_queue(nums: List[int]):
    nums[0] = nums[-1]
    nums.pop()
    pos = 0
    child_pos = 2 * pos + 1
    while pos is not None:
        pos = _swap_child(nums, pos)
    return nums


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = make_priority_queue(nums)
        while len(self.nums) > k:
            self.nums = pop_priority_queue(self.nums)

    def add(self, val: int) -> int:
        self.nums = push_priority_queue(self.nums, val)
        if len(self.nums) > self.k:
            self.nums = pop_priority_queue(self.nums)
        return self.nums[0]
