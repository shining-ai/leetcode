# Backtracking
# 再帰が深いので、stackで書き直した
class Solution:
    def combinationSum(
        self, candidates: List[int], target: int) -> List[List[int]]:
        stack = [(target, [], 0)]
        combinations = []
        while stack:
            before_remain, before_combination, begin = stack.pop()
            for i in range(begin, len(candidates)):
                remain = before_remain - candidates[i]
                combination = before_combination + [candidates[i]]
                if remain == 0:
                    combinations.append(combination)
                elif 0 < remain:
                    stack.append((remain, combination, i))
        return combinations
