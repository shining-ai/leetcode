class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [("", n, n)]
        parentheses = []
        while stack:
            current, remain_left, remain_right = stack.pop()
            if remain_left == 0 and remain_right == 0:
                parentheses.append(current)
                continue
            if 0 < remain_left:
                stack.append((current + "(", remain_left - 1, remain_right))
            if remain_left < remain_right:
                stack.append((current + ")", remain_left, remain_right - 1))

        return parentheses


# backtracking
# 関数内で使う変数は先に定義する
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []

        def make_combination(current, remain_left, remain_right):
            if remain_left == 0 and remain_right == 0:
                parentheses.append(current)
                return
            if 0 < remain_left:
                make_combination(current + "(", remain_left - 1, remain_right)
            if remain_left < remain_right:
                make_combination(current + ")", remain_left, remain_right - 1)

        make_combination("", n, n)
        return parentheses
