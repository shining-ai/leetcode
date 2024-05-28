# 左から高さを確認していき、高さが減少するタイミングでその高さより高い場合の面積を計算する。
# [3, 5, 2, 6]の場合、2に到達した時に高さが減少するので、それより左側にある2より高い3と5の面積を計算する。
# 5のとき: 5 * 1 = 5
# 3のとき: 3 * 2 = 6
# 端まで到達したら、計算されなかった要素で計算する。
# 2のとき: 2 * 4 = 6
# 6のとき: 6 * 1 = 6
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for end in range(len(heights)):
            start = end
            while stack and stack[-1][1] > heights[end]:
                start, height = stack.pop()
                max_area = max(max_area, height * (end - start))
            stack.append([start, heights[end]])
        while stack:
            start, height = stack.pop()
            max_area = max(max_area, height * (len(heights) - start))
        return max_area
