# backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def make_combination(current):
            if remain["("] > remain[")"]:
                return
            if remain["("] < 0:
                return
            if remain[")"] == 0:
                parentheses.append(current)
                return
            for bracket in brackets:
                remain[bracket] -= 1
                make_combination(current + bracket)
                remain[bracket] += 1

        brackets = ["(", ")"]
        remain = {"(": n, ")": n}
        parentheses = []
        make_combination("")
        return parentheses
