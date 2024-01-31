class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(": ")", "[": "]", "{": "}"}
        for i_char in s:
            if i_char in mapping:
                stack.append(i_char)
                continue
            if not stack:
                return False
            if i_char != mapping[stack[-1]]:
                return False
            stack.pop()
        if stack:
            return False
        return True
