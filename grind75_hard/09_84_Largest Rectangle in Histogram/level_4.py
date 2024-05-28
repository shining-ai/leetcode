# segment treeを書き直した
# rootのindexは1
# 親ノード: i // 2
# 子ノード: (i * 2), (i * 2 + 1)
class SegmentTree:
    def __init__(self, nums):
        self.size = 1
        while self.size < len(nums):
            self.size *= 2
        self.tree = [(float("inf"), 0)] * (self.size * 2)
        # 葉ノードに値をセット
        for i, num in enumerate(nums):
            self.tree[self.size + i] = (num, i)
        # 葉ノード以外に最小値をセット
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    # 最上段から下がっていき、[begin, end)の最小値を取得
    # [node_begin, node_end)が現在のノードの区間
    def query(self, begin, end, node=1, node_begin=0, node_end=-1):
        if node_end == -1:
            node_end = self.size
        if node_end <= begin or end <= node_begin:  # 対象区間が被らない
            return (float("inf"), 0)
        if begin <= node_begin and node_end <= end:  # 対象区間が完全に被る
            return self.tree[node]
        # 一部だけ被る  -> 子ノードに問い合わせ
        node_middle = (node_begin + node_end) // 2
        left_min = self.query(begin, end, node * 2, node_begin, node_middle)
        right_min = self.query(begin, end, node * 2 + 1, node_middle, node_end)
        return min(left_min, right_min)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        segment_tree = SegmentTree(heights)

        def calc_area(begin, end):
            if begin >= end:
                return 0
            min_value, min_index = segment_tree.query(begin, end)
            area = min_value * (end - begin)
            max_area = max(
                area, calc_area(begin, min_index), calc_area(min_index + 1, end)
            )
            return max_area

        return calc_area(0, len(heights))


# stackを使った解法に番兵を利用
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        heights.append(0)
        stack = []
        for end in range(len(heights)):
            start = end
            while stack and stack[-1][1] >= heights[end]:
                start, height = stack.pop()
                max_area = max(max_area, height * (end - start))
            stack.append([start, heights[end]])
        return max_area
