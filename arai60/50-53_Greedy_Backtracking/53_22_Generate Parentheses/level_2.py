# backtracking
# 括弧の数を引数にする
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def make_combination(current, remain_left, remain_right):
            if remain_left == 0 and remain_right == 0:
                parentheses.append(current)
                return
            if 0 < remain_left:
                make_combination(current + "(", remain_left - 1, remain_right)
            if remain_left < remain_right:
                make_combination(current + ")", remain_left, remain_right - 1)

        parentheses = []
        make_combination("", n, n)
        return parentheses
