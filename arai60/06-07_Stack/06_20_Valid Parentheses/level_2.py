class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {"(": ")", "[": "]", "{": "}"}
        for i_char in s:
            if i_char in bracket_pairs:
                stack.append(i_char)
                continue
            if not stack:
                return False
            if i_char != bracket_pairs[stack[-1]]:
                return False
            stack.pop()
        if stack:
            return False
        return True
