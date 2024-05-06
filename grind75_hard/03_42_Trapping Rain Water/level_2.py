# DPを使って解く
# brute forceと同じ考え方だが、左右の壁の最大値を記憶しておく
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)  # [0,i]の範囲の最大値
        max_right = [0] * len(height)  # [i,length)の範囲の最大値
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i])
            max_right[-i - 1] = max(max_right[-i], height[-i - 1])
        total_water = 0
        for i in range(1, len(height) - 1):
            water_height = min(max_left[i], max_right[i])
            total_water += water_height - height[i]
        return total_water
