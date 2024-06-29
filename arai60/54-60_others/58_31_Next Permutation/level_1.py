# 1 4 3 2
# 右から見ていき、初めて小さくなる部分を見つける(この場合1)
# 1より右側で、1より大きい最小の数を見つける(この場合2)
# 2つを入れ替える
# 2 4 3 1
# 2より右側を昇順にソートする
# 2 1 3 4
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for left in range(len(nums) - 2, -1, -1):
            if nums[left] < nums[left + 1]:
                right_min = math.inf
                for i in range(left + 1, len(nums)):
                    if nums[left] < nums[i] < right_min:
                        right_min = nums[i]
                        right = i
                nums[left], nums[right] = nums[right], nums[left]
                nums[left + 1 :] = sorted(nums[left + 1 :])
                break
        else:
            nums.reverse()
