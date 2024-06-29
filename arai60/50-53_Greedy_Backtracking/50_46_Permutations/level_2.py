# 順列を昇順に作成していく
# 1 4 3 2
# 右から見ていき、初めて小さくなる部分を見つける(この場合1)
# 1より右側で、1より大きい最小の数を見つける(この場合2)
# 2つを入れ替える
# 2 4 3 1
# 2より右側を昇順にソートする
# 2 1 3 4
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def make_next_permutation(nums):
            for left in range(len(nums) - 2, -1, -1):
                if nums[left] < nums[left + 1]:
                    break
            else:
                return False

            min_right_num = math.inf
            for i in range(left + 1, len(nums)):
                if nums[left] < nums[i] < min_right_num:
                    min_right_num = nums[i]
                    right = i
            nums[left], nums[right] = nums[right], nums[left]
            nums[left + 1 :] = sorted(nums[left + 1 :])
            return True

        nums_copy = nums[:]
        nums_copy.sort()
        permutations = [nums_copy[:]]
        while make_next_permutation(nums_copy):
            permutations.append(nums_copy[:])
        return permutations
