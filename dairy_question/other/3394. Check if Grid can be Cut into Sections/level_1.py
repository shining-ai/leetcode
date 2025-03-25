# ソートして解く
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_cat(rectangles, dim):
            gap_count = 0
            rectangles.sort(key=lambda rect: rect[dim])
            farthest_end = rectangles[0][dim + 2]
            for i in range(1, len(rectangles)):
                if farthest_end <= rectangles[i][dim]:
                    gap_count += 1
                farthest_end = max(farthest_end, rectangles[i][dim + 2])
            return gap_count >= 2

        return can_cat(rectangles, 0) or can_cat(rectangles, 1)
