# Space: O(1)
# 左右からポインタをずらしていく
# 片方のポインタは今までの最大値で止まるようにしておく
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        left = 0
        right = len(height) - 1
        total_water = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                right -= 1
        return total_water


# DPを使って解く
# 変数名を修正
class Solution:
    def trap(self, height: List[int]) -> int:
        max_heights_in_left = [0] * len(height)  # [0,i]の範囲の最大値
        max_heights_in_right = [0] * len(height)  # [i,length)の範囲の最大値
        max_heights_in_left[0] = height[0]
        max_heights_in_right[-1] = height[-1]
        for i in range(1, len(height)):
            max_heights_in_left[i] = max(max_heights_in_left[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            max_heights_in_right[i] = max(max_heights_in_right[i + 1], height[i])
        total_water = 0
        for i in range(1, len(height) - 1):
            water_height = min(max_heights_in_left[i], max_heights_in_right[i])
            total_water += water_height - height[i]
        return total_water
