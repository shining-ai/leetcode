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
