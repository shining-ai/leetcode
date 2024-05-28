class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for end in range(len(heights)):
            start = end
            while stack and stack[-1][1] > heights[end]:
                start, height = stack.pop()
                area = height * (end - start)
                max_area = max(max_area, area)
            stack.append((start, heights[end]))
        while stack:
            start, height = stack.pop()
            area = height * (len(heights) - start)
            max_area = max(max_area, area)
        return max_area
