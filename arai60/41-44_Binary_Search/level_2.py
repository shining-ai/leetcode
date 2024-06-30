# 場合分けをして1回の2分探索で処理する
# case1(左の塊で折り返し) : 8 9 1 2   3   4 5 6 7
# case2(右の塊で折り返し) : 3 4 5 6   7   8 9 1 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            # case1
            if nums[middle] < nums[right]:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            # case2
            else:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1
