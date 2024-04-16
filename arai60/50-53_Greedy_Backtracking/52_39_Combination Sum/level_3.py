sys.setrecursionlimit(2000)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def make_combinations(remain, combination, begin):
            if remain < 0:
                return
            if remain == 0:
                combinations.append(combination[:])
                return
            for i in range(begin, len(candidates)):
                combination.append(candidates[i])
                make_combinations(remain - candidates[i], combination, i)
                combination.pop()

        combinations = []
        make_combinations(target, [], 0)
        return combinations
