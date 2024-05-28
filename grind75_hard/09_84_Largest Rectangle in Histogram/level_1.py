# 総当たり(TLE)
# O(N^3)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rectangle = [0] * len(heights)
        for i in range(len(heights)):
            for j in range(i + 1, len(heights) + 1):
                rectangle = min(heights[i:j]) * (j - i)
                max_rectangle[i] = max(max_rectangle[i], rectangle)
        return max(max_rectangle)


# 最小値の判定を効率化した総当たり(TLE)
# O(N^2)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rectangle = [0] * len(heights)
        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                rectangle = min_height * (j - i + 1)
                max_rectangle[i] = max(max_rectangle[i], rectangle)
        return max(max_rectangle)


# 最小値で左右に分割してそれぞれを比較(TLE)
# O(NlogN)
# ソートされている時はO(N^2)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calc_area(left, right):
            if left >= right:
                return 0
            min_value = float("inf")
            for i in range(left, right):
                if min_value < heights[i]:
                    continue
                min_value = heights[i]
                min_index = i
            area = min_value * (right - left)
            max_area = max(
                area, calc_area(left, min_index), calc_area(min_index + 1, right)
            )
            return max_area

        return calc_area(0, len(heights))


# 最小値をsegment treeで管理して効率化
# O(NlogN)
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [None] * (2 * self.n)
        for i, num in enumerate(nums):
            self.tree[self.n + i] = (num, i)
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, left, right):
        left += self.n
        right += self.n
        min_value_index = (float("inf"), 0)
        while left < right:
            if left % 2 == 1:
                min_value_index = min(min_value_index, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                min_value_index = min(min_value_index, self.tree[right])
            left //= 2
            right //= 2
        return min_value_index[0], min_value_index[1]


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        segment_tree = SegmentTree(heights)

        def calc_area(left, right):
            if left >= right:
                return 0
            min_value, min_index = segment_tree.query(left, right)
            area = min_value * (right - left)
            max_area = max(
                area, calc_area(left, min_index), calc_area(min_index + 1, right)
            )
            return max_area

        return calc_area(0, len(heights))
