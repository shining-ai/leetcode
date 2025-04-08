# DPを使って解く
# 変数名を修正
# max_height_in_rightはmax_heights_in_leftとは別のループで構築する
class Solution:
    def trap(self, height: List[int]) -> int:
        max_heights_in_left = [0] * len(height)  # [0,i]の範囲の最大値
        max_height_in_right = [0] * len(height)  # [i,length)の範囲の最大値
        max_heights_in_left[0] = height[0]
        max_height_in_right[-1] = height[-1]
        for i in range(1, len(height)):
            max_heights_in_left[i] = max(max_heights_in_left[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            max_height_in_right[i] = max(max_height_in_right[i + 1], height[i])
        total_water = 0
        for i in range(1, len(height) - 1):
            water_height = min(max_heights_in_left[i], max_height_in_right[i])
            total_water += water_height - height[i]
        return total_water


# stackを使って実装
# 変数名を修正
class Solution:
    def trap(self, height: List[int]) -> int:
        left_wall_indexes = []
        total_water = 0
        for right in range(len(height)):
            while left_wall_indexes and height[left_wall_indexes[-1]] <= height[right]:
                bottom_index = left_wall_indexes.pop()
                if not left_wall_indexes:
                    break
                left = left_wall_indexes[-1]
                distance = right - left - 1
                depth = min(height[left], height[right]) - height[bottom_index]
                total_water += distance * depth
            left_wall_indexes.append(right)
        return total_water
