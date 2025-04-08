# brute force
# 現在地より左側の最大値が左の壁、右側の最大値が右の壁となる。
# 現在地の水位は、左右の壁の小さいほうになる。
# 現在地が壁より低ければ、水が貯まる。
# O(n^2)
class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        for i in range(1, len(height) - 1):  # 両端には水が貯まらないので除外
            left_wall = max(height[:i])
            right_wall = max(height[i + 1 :])
            water_height = min(left_wall, right_wall)
            if water_height < height[i]:
                continue
            total_water += water_height - height[i]
        return total_water


# stackを使って実装
# 左側の壁をstackで記憶し、右側の壁が見つかったら、貯まる水を計算する。
class Solution:
    def trap(self, height: List[int]) -> int:
        left_walls = []
        total_water = 0
        for right in range(len(height)):
            while left_walls and height[left_walls[-1]] <= height[right]:
                bottom_index = left_walls.pop()
                if not left_walls:
                    break
                left = left_walls[-1]
                distance = right - left - 1
                depth = min(height[left], height[right]) - height[bottom_index]
                total_water += distance * depth
            left_walls.append(right)
        return total_water
