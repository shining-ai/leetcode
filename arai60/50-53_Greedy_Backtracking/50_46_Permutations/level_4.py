# leftの位置探索をwhile文に修正
# permutationsの初期値をループ内に移動
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def make_next_permutation(nums):
            left = len(nums) - 2
            while 0 <= left:
                if nums[left] < nums[left + 1]:
                    break
                left -= 1
            else:
                return False

            min_right_num = math.inf
            for i in range(left + 1, len(nums)):
                if nums[left] < nums[i] < min_right_num:
                    min_right_num = nums[i]
                    right = i
            nums[left], nums[right] = nums[right], nums[left]
            nums[left + 1 :] = reversed(nums[left + 1 :])
            return True

        current_pamutation = nums[:]
        current_pamutation.sort()
        permutations = []
        while True:
            permutations.append(current_pamutation[:])
            if not make_next_permutation(current_pamutation):
                break
        return permutations
