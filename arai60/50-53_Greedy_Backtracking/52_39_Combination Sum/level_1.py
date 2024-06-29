# Backtracking
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def make_combination(remain, current, begin):
            if remain == 0:
                combinations.append(current[:])
                return
            if remain < 0:
                return
            for i in range(begin, len(candidates)):
                current.append(candidates[i])
                make_combination(remain - candidates[i], current, i)
                current.pop()

        combinations = []
        make_combination(target, [], 0)
        return combinations
