class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {"(": ")", "[": "]", "{": "}"}
        for bracket in s:
            if bracket in bracket_pairs:
                stack.append(bracket)
                continue
            if not stack:
                return False
            if bracket != bracket_pairs[stack[-1]]:
                return False
            stack.pop()
        return not stack
