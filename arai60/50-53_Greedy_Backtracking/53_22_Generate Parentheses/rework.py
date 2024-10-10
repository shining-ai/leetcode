class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        patterns = []

        def helper(current, left_remain, right_remain):
            if left_remain == 0 and right_remain == 0:
                patterns.append(current)
                return
            if 0 < left_remain:
                helper(current + "(", left_remain - 1, right_remain)
            if left_remain < right_remain:
                helper(current + ")", left_remain, right_remain - 1)

        helper("", n, n)
        return patterns
